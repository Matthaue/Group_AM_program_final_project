import pandas as pd
import json

def excel_to_json(excel_path, json_path):
    # 读取多重表头，前两行 header=[0, 1]
    df = pd.read_excel(excel_path, header=[0, 1])

    # 获取所有起点及其每组三列的起始索引
    columns = list(df.columns)
    start_points = []
    start_col_info = []
    for idx in range(1, len(columns), 3):
        start_point = columns[idx][0].strip()
        start_points.append(start_point)
        start_col_info.append(idx)

    # 终点为第一列
    end_points = df.iloc[:, 0].tolist()

    data = {}
    for s_idx, sp in enumerate(start_points):
        data[sp] = {}
        col_base = start_col_info[s_idx]
        for row_idx, ep in enumerate(end_points):
            price = df.iloc[row_idx, col_base]
            distance = df.iloc[row_idx, col_base + 1]
            time = df.iloc[row_idx, col_base + 2]
            # 跳过空数据
            if pd.isnull(price) and pd.isnull(distance) and pd.isnull(time):
                continue
            data[sp][ep] = {
                "price_yuan": None if pd.isnull(price) else float(price),
                "distance_km": None if pd.isnull(distance) else float(distance),
                "time_min": None if pd.isnull(time) else int(time)
            }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Convert Excel fare table to JSON.")
    parser.add_argument("excel_file", help="Path to Excel file")
    parser.add_argument("json_file", help="Path to output JSON")
    args = parser.parse_args()
    excel_to_json(args.excel_file, args.json_file)