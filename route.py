import numpy as np
import json
from data import ScenicData

class RoutePlanner:
    def __init__(self, data_path, coord_path=None, mode='distance'):
        """
        :param data_path: 景点之间距离/时间/价格数据（如 cleaned_data.json）
        :param coord_path: 景点坐标与元数据（如 spots_info.json，可选，若无坐标解析则忽略此参数）
        :param mode: 'distance', 'time', or 'price'
        """
        self.data = ScenicData(data_path)
        self.spot_names = self.data.get_spot_names()
        self.distance_matrix = self.data.get_matrix('distance')
        self.time_matrix = self.data.get_matrix('time')
        self.price_matrix = self.data.get_matrix('price')
        self.matrix = self.data.get_matrix(mode)
        self.n = len(self.spot_names)
        self.coords = {}
        if coord_path:
            self._load_coords(coord_path)
        self.mode = mode

    def _load_coords(self, coord_path):
        """读取含坐标的景点信息（可选）"""
        try:
            with open(coord_path, 'r', encoding='utf-8') as f:
                info_data = json.load(f)
            for spot in info_data:
                self.coords[spot['name']] = spot.get('coord', None)
        except Exception as e:
            self.coords = {}

    def _filter_spots(self, must_visit, can_visit, not_visit, start, end):
        """生成参与运算的有效景点下标集合"""
        # 转景点名为下标
        must_idxs = [self.data.get_spot_index(x) for x in must_visit if self.data.get_spot_index(x) is not None]
        can_idxs = [self.data.get_spot_index(x) for x in can_visit if self.data.get_spot_index(x) is not None]
        not_idxs = set([self.data.get_spot_index(x) for x in not_visit if self.data.get_spot_index(x) is not None])
        start_idx = self.data.get_spot_index(start)
        end_idx = self.data.get_spot_index(end)
        # 不可去景点排除
        all_idxs = set(must_idxs + can_idxs)
        valid_idxs = [i for i in all_idxs if i not in not_idxs]
        # 起终点也要纳入有效集合
        if start_idx is not None:
            valid_idxs.append(start_idx)
        if end_idx is not None and end_idx != start_idx:
            valid_idxs.append(end_idx)
        valid_idxs = list(sorted(set(valid_idxs)))  # 去重排序
        return valid_idxs, start_idx, end_idx

    def plan_route(self, start, end, must_visit=None, can_visit=None, not_visit=None,
                   max_time=None, max_dist=None, max_price=None):
        """
        核心接口，输入参数后自动选择算法并返回路线结果
        """
        must_visit = must_visit or []
        can_visit = can_visit or []
        not_visit = not_visit or []

        idxs, start_idx, end_idx = self._filter_spots(must_visit, can_visit, not_visit, start, end)
        if start_idx is None or end_idx is None:
            return {"error": "起点或终点不存在，请检查名称"}
        # 必去景点是否都有效
        if len(must_visit) > 0 and any(self.data.get_spot_index(x) is None for x in must_visit):
            return {"error": "部分必去景点名称无效"}

        sub_matrix = self.matrix[np.ix_(idxs, idxs)]
        sub_spots = [self.spot_names[i] for i in idxs]
        must_relative = [sub_spots.index(must) for must in must_visit if must in sub_spots]
        start_rel = sub_spots.index(self.spot_names[start_idx])
        end_rel = sub_spots.index(self.spot_names[end_idx])

        sub_dist = self.distance_matrix[np.ix_(idxs, idxs)]
        sub_time = self.time_matrix[np.ix_(idxs, idxs)]
        sub_price = self.price_matrix[np.ix_(idxs, idxs)]

        # 判断是TSP型还是部分点+约束型
        full_tsp = (len(must_visit) + len(can_visit) == len(idxs) - (1 if start_idx == end_idx else 2))
        route, cost = None, np.inf
        if full_tsp and start_idx == end_idx:
            route, cost = self._tsp(sub_matrix, start_rel)
        else:
            route, cost = self._backtrack(
                sub_matrix, start_rel, end_rel, must_relative,
                max_time, max_dist, max_price, sub_time, sub_dist, sub_price
            )
        if route is None:
            return {"error": "无可行路线或约束过严"}

        # 计算总距离、总时间、总价格
        total_distance = 0
        total_time = 0
        total_price = 0
        for i in range(len(route) - 1):
            a, b = route[i], route[i+1]
            total_distance += sub_dist[a, b]
            total_time += sub_time[a, b]
            total_price += sub_price[a, b]

        step_routes = []
        for i in range(len(route) - 1):
            from_name = sub_spots[route[i]]
            to_name = sub_spots[route[i+1]]
            info = self.data.get_route_info(from_name, to_name)
            step_routes.append({
                "from": from_name,
                "to": to_name,
                "public_transport_route": info.get('public_transport', {}).get('route') if info else None,
                "distance_km": info.get('public_transport', {}).get('distance_km') if info else None,
                "time_min": info.get('public_transport', {}).get('time_min') if info else None,
                "taxi_price_yuan": info.get('taxi', {}).get('price_yuan') if info else None
            })

        result = {
            "route": [sub_spots[i] for i in route],
            "steps": step_routes,
            "total_time_min": total_time,
            "total_distance_km": total_distance,
            "total_price_yuan": total_price,
            "success": True
        }
        return result

    def _tsp(self, matrix, start_idx):
        import itertools
        n = matrix.shape[0]
        idxs = list(range(n))
        best_cost = np.inf
        best_route = None
        for perm in itertools.permutations([i for i in idxs if i != start_idx], n - 1):
            route = [start_idx] + list(perm) + [start_idx]
            cost = 0
            broken = False
            for i in range(n):
                a, b = route[i], route[i+1]
                if np.isinf(matrix[a, b]):
                    broken = True
                    break
                cost += matrix[a, b]
                if cost >= best_cost:
                    broken = True
                    break
            if not broken and cost < best_cost:
                best_cost = cost
                best_route = route
        return best_route, best_cost

    def _backtrack(self, matrix, start_rel, end_rel, must_relative,
                   max_time=None, max_dist=None, max_price=None,
                   time_matrix=None, dist_matrix=None, price_matrix=None):
        n = matrix.shape[0]
        best_cost = np.inf
        best_route = None

        def dfs(cur, visited, route, cost, time_sum, dist_sum, price_sum):
            nonlocal best_cost, best_route
            if (max_time is not None and time_sum > max_time) or \
               (max_dist is not None and dist_sum > max_dist) or \
               (max_price is not None and price_sum > max_price):
                return
            if cur == end_rel and all(visited[i] for i in must_relative) and len(route) > 1:
                if cost < best_cost:
                    best_cost = cost
                    best_route = list(route)
                return
            for nxt in range(n):
                if visited[nxt] or np.isinf(matrix[cur, nxt]) or cur==nxt:
                    continue
                visited[nxt] = True
                route.append(nxt)
                dfs(nxt, visited, route,
                    cost + matrix[cur, nxt],
                    time_sum + (time_matrix[cur, nxt] if time_matrix is not None else 0),
                    dist_sum + (dist_matrix[cur, nxt] if dist_matrix is not None else 0),
                    price_sum + (price_matrix[cur, nxt] if price_matrix is not None else 0))
                route.pop()
                visited[nxt] = False

        visited = [False] * n
        visited[start_rel] = True
        dfs(start_rel, visited, [start_rel], 0, 0, 0, 0)
        return best_route, best_cost

def get_route_json(data_path, user_input_json_path):
    """
    指定输入json文件，返回路线规划json结果
    """
    with open(user_input_json_path, 'r', encoding='utf-8') as f:
        user_input = json.load(f)
    planner = RoutePlanner(data_path, mode=user_input.get('mode', 'distance'))
    res = planner.plan_route(
        start=user_input['start'],
        end=user_input['end'],
        must_visit=user_input.get('must_visit', []),
        can_visit=user_input.get('can_visit', []),
        not_visit=user_input.get('not_visit', []),
        max_time=user_input.get('max_time', None),
        max_dist=user_input.get('max_dist', None),
        max_price=user_input.get('max_price', None)
    )
    return res

import sys
def save_route_result(result, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="旅游路线规划")
    parser.add_argument('--data', type=str, default='data/cleaned_data.json', help='景点数据路径')
    parser.add_argument('--user_input', type=str, default='data/user_input.json', help='用户输入数据路径')
    parser.add_argument('--output', type=str, default='output/route_result.json', help='输出结果json文件路径')
    args = parser.parse_args()

    result = get_route_json(args.data, args.user_input)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    save_route_result(result, args.output)