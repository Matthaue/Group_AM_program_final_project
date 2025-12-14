import json

def merge_routes_and_taxi(transport_json, taxi_json, output_json):
    with open(transport_json, 'r', encoding='utf-8') as f:
        transport = json.load(f)
    with open(taxi_json, 'r', encoding='utf-8') as f:
        taxi = json.load(f)

    merged = {}
    # 按出行起点整合
    for start in transport:
        merged[start] = {}
        # 收集所有终点（公共+出租合并保证全覆盖）
        endpoints = set()
        if start in taxi:
            endpoints.update(taxi[start].keys())
        endpoints.update(transport[start].keys())
        for end in endpoints:
            seg = {}
            # 地铁/公交部分
            if end in transport[start]:
                seg['public_transport'] = transport[start][end]
            # 打车部分
            if start in taxi and end in taxi[start]:
                seg['taxi'] = taxi[start][end]
            merged[start][end] = seg

    # 处理：出租车有但地铁/公交完全没有的起点情况（不常见但容错）
    for start in taxi.keys():
        if start not in merged:
            merged[start] = {}
        for end in taxi[start].keys():
            if end not in merged[start]:
                merged[start][end] = {'taxi': taxi[start][end]}

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Merge public transport and taxi route JSONs.")
    parser.add_argument('public_transport_json', help='public_transport.json 文件路径')
    parser.add_argument('taxi_json', help='taxi.json 文件路径')
    parser.add_argument('output_json', help='合并后的数据输出文件名，如 merged.json')
    args = parser.parse_args()
    merge_routes_and_taxi(args.public_transport_json, args.taxi_json, args.output_json)