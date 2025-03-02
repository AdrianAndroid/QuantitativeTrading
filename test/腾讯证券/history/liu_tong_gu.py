import csv
import time
import pandas as pd
import os
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


def is_file_exists(file_path):
    # 使用 os.path.exists() 检查路径是否存在
    return os.path.exists(file_path) and os.path.isfile(file_path)


def is_dir_exists(file_path):
    return os.path.exists(file_path) and not os.path.isfile(file_path)


def get_time_stamp():
    timestamp_13 = int(time.time() * 1000)
    return timestamp_13


# https://proxy.finance.qq.com/ifzqgtimg/appstock/hs/ltgd/get?type=ltgd&_var=v_liutonggd&code=sh603288&_=1740738469487
def url_history(stock):
    timestamp = get_time_stamp()
    url = f"https://proxy.finance.qq.com/ifzqgtimg/appstock/hs/ltgd/get?type=ltgd&_var=v_liutonggd&code={stock}&_={timestamp}"
    print(f'url = {url}')
    return url


def read_url_to_json(url):
    try:
        resp = request.urlopen(url, timeout=10)
        data = resp.read()
        decode_data = data.decode('utf-8')
        json_decode_data = decode_data.split('=', 1)[1]
        json_data = json.loads(json_decode_data)
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


def save_json_to_file(json_data, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)


def read_stock_csv(callback):
    filepath = local_dir_name('stocks.csv')
    df = pd.read_csv(filepath, dtype={0: str})
    for index, row in df.iterrows():
        _code = row[0]
        _name = row[1]
        _type = row[2]
        # print(f'{_type} {_code} {_name}')
        callback(_code, _name, _type)


def read_stock_csv_2(callback):
    filepath = local_dir_name('stocks.csv')
    df = pd.read_csv(filepath, dtype={0: str})
    size = len(df)
    for index, row in df.iterrows():
        _code = row[0]
        _name = row[1]
        _type = row[2]
        # print(f'{_type} {_code} {_name}')
        callback(_code, _name, _type)
        print(size)
        size -= 1


def process_program(_code, _name, _type):
    local_file_path = f'{_type}{_code}.json'
    if is_file_exists(local_file_path):
        print(f'{local_file_path} 存在，公司名称是：{_name}')
        return
    _url = url_history(f'{_type}{_code}')
    json_data = read_url_to_json(_url)
    if json_data is not None:
        save_json_to_file(json_data, file_name=local_file_path)
        print(f'保存文件：{local_file_path}, 公司名称：{_name}')
    time.sleep(0.1)


# https://proxy.finance.qq.com/ifzqgtimg/appstock/hs/ltgd/get?type=ltgd&_var=v_liutonggd&code=sh603288&_=1740738469487
# 1740738469487
# 1740739969712


if __name__ == "__main__":
    read_stock_csv_2(process_program)
