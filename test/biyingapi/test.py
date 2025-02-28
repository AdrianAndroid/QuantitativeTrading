import json

import json
import csv

json_data0 = '''
    {}
'''

# 示例嵌套 JSON 数据
json_data = '''
[
    {
        "person": {
            "name": "Alice",
            "age": 25
        },
        "city": "New York"
    },
    {
        "person": {
            "name": "Bob",
            "age": 30
        },
        "city": "Los Angeles"
    }
]
'''
json_data2 = '''
    {
        "person": {
            "name": "Alice",
            "age": 25
        },
        "city": "New York"
    }
'''

try:

    data = json.loads(json_data0)
    print(isinstance(data, dict))
    print(len(data) > 0)
    print("--------------")
    print("--------------")
    print("--------------")
    print("--------------")
    # 解析 JSON 数据
    data = json.loads(json_data)
    print(data)
    if isinstance(data, list) and len(data) > 0:
        print("is JsonArray")
        print('jsonarray', len(data))
        keys = list(data[0].keys())
        print("jsonarray", type(keys), keys)
        for row in data:
            print(row)

    print("--------------")
    print("--------------")
    print("--------------")
    print("--------------")
    data = json.loads(json_data2)
    if isinstance(data, dict):
        print("is JsonObject")
        keys = list(data.keys())
        print('array', type(keys), keys)
    print(data)
except json.JSONDecodeError as e:
    print(f"JSON 解析错误: {e}")
else:
  pass
    # 定义 CSV 文件的列名
    # fieldnames = data[0].keys
    # print('fieldnames', fieldnames)
    # 打开 CSV 文件并写入数据
    # with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #     writer = csv.writer(csvfile)
    #     # 写入表头
    #     # writer.writeheader()
    #     # 处理嵌套数据并写入 CSV
    #     for row in data:
    #         writer.writerow(row)
