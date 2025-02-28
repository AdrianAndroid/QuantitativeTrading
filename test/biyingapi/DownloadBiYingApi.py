import csv
import json
import time
from urllib import request
from urllib.error import URLError, HTTPError
import os
import socket  # Import socket to handle timeout exceptions


def local_dir_name(file_name):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return current_directory + '/' + file_name


def read_url_to_json(url):
    try:
        resp = request.urlopen(url, timeout=10)
        data = resp.read()
        decode_data = data.decode('utf-8')
        json_data = json.loads(decode_data)
    except HTTPError as e:
        print(f"HTTP 错误: {e.code}, URL: {url}")
        return None
    except URLError as e:
        print(f"URL 错误: {e.reason}, URL: {url}")
        return None
    except socket.timeout as e:
        print(f"请求超时: {url}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON 解码错误:", url)
        return None
    return json_data


def save_json_to_file(json_data, api_name):
    file_name = api_name + '.json'
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)


def is_json_list_not_empty(json):
    return isinstance(json, list) and len(json) > 0


def is_json_dict_not_empty(json):
    return isinstance(json, dict) and len(json) > 0


def write_json_list_to_csv(json_data, api_name):
    csv_file = local_dir_name(api_name) + '.csv'
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = json_data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in json_data:
            writer.writerow(item)


def write_json_dict_to_csv(json_data, api_name):
    csv_file = local_dir_name(api_name) + '.csv'
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = json_data.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(json_data)


def read_config(callback):
    config_file = local_dir_name('config.csv')
    print(config_file)
    with open(config_file, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            apiName = row[0]
            apiUrl = row[1]
            callback(apiName, apiUrl)


def read_config_2(callback):
    dict0 = {
        '最新分时交易数据接口': 'http://api.biyingapi.com/hszb/fsjy/000001/dn/sdfg56655ertghdsf36',
        '最新分时BOLL数据接口': 'http://api.biyingapi.com/hszb/boll/000001/dn/sdfg56655ertghdsf36',
        '沪深两市新股日历': 'http://api.biyingapi.com/hslt/new/sdfg56655ertghdsf36',
        '指数行业概念': 'http://api.biyingapi.com/hszg/list/sdfg56655ertghdsf36',
        '涨停股池': 'http://api.biyingapi.com/hslt/ztgc/2022-09-08/sdfg56655ertghdsf36',
        '公司简介': 'http://api.biyingapi.com/hscp/gsjj/000001/sdfg56655ertghdsf36',
        '历届监事会成员': 'http://api.biyingapi.com/hscp/ljjj/000001/sdfg56655ertghdsf36',
        '财务指标': 'http://api.biyingapi.com/hscp/cwzb/000001/sdfg56655ertghdsf36',
        '十大流通股东': 'http://api.biyingapi.com/hscp/ltgd/000001/sdfg56655ertghdsf36'
    }
    for key in dict0.keys():
        print(key, dict0[key])
    print("------")
    for key, value in dict0.items():
        print(key, value)
        callback(key, value)
    # with open(config_file, 'r', encoding='utf-8', newline='') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         apiName = row[0]
    #         apiUrl = row[1]
    #         callback(apiName, apiUrl)


def process_program(api_name, api_url):
    print(api_name, api_url)
    json_data = read_url_to_json(api_url)
    if json_data is None:
        print('json_data' + api_name + ' is None')
        pass
    save_json_to_file(json_data, api_name)
    if is_json_list_not_empty(json_data):
        write_json_list_to_csv(json_data, api_name)
    elif is_json_dict_not_empty(json_data):
        write_json_dict_to_csv(json_data, api_name)
    else:
        print('json data is empty')
    time.sleep(1)  # 休眠1秒


if __name__ == '__main__':
    # read_config(process_program)
    read_config_2(process_program)
    # 实时交易数据接口,http://api.biyingapi.com/hsrl/ssjy/000001/sdfg56655ertghdsf36
    # process_program('实时交易数据接口', 'http://api.biyingapi.com/hsrl/ssjy/000001/sdfg56655ertghdsf36')
