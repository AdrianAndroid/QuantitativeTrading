import pandas as pd
import os
import json
import sys
import random
from urllib import request
from urllib.error import URLError, HTTPError
import os
import socket  # Import socket to handle timeout exceptions
import datetime
import time

STOCK_PATH = '/Users/zhaojian/code/trading/QuantitativeTrading/test/腾讯证券/history/stocks.csv'
DAYS_PATH = '/Users/zhaojian/code/trading/QuantitativeTrading/test/腾讯证券/history/days'
HISTORY_PATH = '/Users/zhaojian/code/trading/QuantitativeTrading/test/腾讯证券/history/jsons'


def stock_history_filepath(_code, _name, _type):
    history = f'{HISTORY_PATH}/{_type}{_code}.json'
    return history


def is_file_exits(filepath):
    return os.path.exists(filepath) and os.path.isfile(filepath)


def load_json_history_list(history_file_path):
    isFileExits = is_file_exits(history_file_path)
    if not isFileExits:
        return list()
    with open(history_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    if 'data' not in json_data:
        return list()
    data = json_data['data']
    if 'history' not in data:
        return list()
    return data['history']


def day_url(_code, _year):
    return f'https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param={_code},day,{_year}-01-01,{_year}-12-31,320,&r={random.random():.16f}'


def read_stock_csv_2(callback):
    filepath = STOCK_PATH
    df = pd.read_csv(filepath, dtype={0: str})
    size = len(df)
    for index, row in df.iterrows():
        _code = row[0]
        _name = row[1]
        _type = row[2]
        # print(_code, _name, _type)
        callback(_code, _name, _type)
        print(size)
        size -= 1


def read_url(url, _time=3):
    try:
        resp = request.urlopen(url, timeout=10)
        data = resp.read()
        decode_data = data.decode('utf-8')
    except HTTPError as e:
        return read_url_retry(url, _time, f"HTTP 错误: {e.code}, URL: {url}")
    except URLError as e:
        return read_url_retry(url, _time, f"URL 错误: {e.reason}, URL: {url}")
    except socket.timeout as e:
        return read_url_retry(url, _time, f"请求超时:{e}, URL:{url}")
    except Exception as e:
        return read_url_retry(url, _time, f"出现错误:{e}, URL:{url}")
    return decode_data


def read_url_retry(url, _time, msg):
    if _time > 0:
        print(f'重试次数:{_time}', msg)
        if _time > 2:
            time.sleep(5)
        elif _time > 1:
            time.sleep(10)
        else:
            time.sleep(20)
        return read_url(url, _time - 1)
    else:
        return None


def read_url_json(url):
    decodeData = read_url(url)
    json_decode_data = decodeData.split('=', 1)[1]
    json_data = json.loads(json_decode_data)
    time.sleep(0.1)
    return json_data


def save_json_data_path(filename):
    __filepath = f'{DAYS_PATH}/{filename}'
    return __filepath


def save_json_data(__filepath, jsonData):
    if is_file_exits(__filepath):
        print(f'{__filepath} 存在。跳过。')
        pass
    with open(__filepath, 'w', encoding='utf-8') as file:
        json.dump(jsonData, file, ensure_ascii=False, indent=4)


def call_back(_code, _name, _type):
    typeCode = f'{_type}{_code}'
    # 读取stock.json
    s_h_f_p = stock_history_filepath(_code, _name, _type)
    # 读取json中的history内容
    loadJsonHistoryList = load_json_history_list(s_h_f_p)
    print(loadJsonHistoryList)
    if not isinstance(loadJsonHistoryList, list):
        pass
    _year = datetime.date.today().year
    dayUrl = day_url(typeCode, _year)
    # print(readUrlData)
    day_json_file_name = f'{DAYS_PATH}/{typeCode}_{_year}.json'
    if not is_file_exits(day_json_file_name):
        print(dayUrl)
        jsonData = read_url_json(dayUrl)
        save_json_data(day_json_file_name, jsonData)
    for year in loadJsonHistoryList:
        dayUrl = day_url(typeCode, year)
        day_json_file_name = f'{DAYS_PATH}/{typeCode}_{year}.json'
        if not is_file_exits(day_json_file_name):
            print(dayUrl)
            jsonData = read_url_json(dayUrl)
            save_json_data(day_json_file_name, jsonData)


if __name__ == "__main__":
    read_stock_csv_2(call_back)
