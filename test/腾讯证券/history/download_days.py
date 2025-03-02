import random
from urllib import request
from urllib.error import URLError, HTTPError
import os
import socket  # Import socket to handle timeout exceptions


# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,,,320,&r=0.3090699758740716

# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2025-01-01,2025-12-31,320,&r=0.8343595718071068
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2024-01-01,2024-12-31,320,&r=0.8343595718071068
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2023-01-01,2023-12-31,320,&r=0.8343595718071068
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2022-01-01,2022-12-31,320,&r=0.841808357694148
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2021-01-01,2021-12-31,320,&r=0.841808357694148
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2020-01-01,2020-12-31,320,&r=0.841808357694148
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2019-01-01,2019-12-31,320,&r=0.5790024394370668
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2018-01-01,2018-12-31,320,&r=0.5790024394370668
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2017-01-01,2017-12-31,320,&r=0.6479748345149974
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2016-01-01,2016-12-31,320,&r=0.3416984672734773
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2015-01-01,2015-12-31,320,&r=0.3416984672734773
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2014-01-01,2014-12-31,640,&r=0.84390735997577
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2013-01-01,2013-12-31,640,&r=0.84390735997577
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2012-01-01,2013-12-31,640,&r=0.6874497059731408
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2011-01-01,2011-12-31,320,&r=0.372498349161583
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2010-01-01,2010-12-31,320,&r=0.6875399413601004
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2009-01-01,2009-12-31,320,&r=0.5057021477625687
# https://proxy.finance.qq.com/ifzqgtimg/appstock/app/newkline/newkline?_var=kline_day&param=sz002230,day,2008-01-01,2008-12-31,320,&r=0.7532961650919088


def read_url(url):
    try:
        resp = request.urlopen(url, timeout=10)
        data = resp.read()
        decode_data = data.decode('utf-8')
    except HTTPError as e:
        print(f"HTTP 错误: {e.code}, URL: {url}")
        return None
    except URLError as e:
        print(f"URL 错误: {e.reason}, URL: {url}")
        return None
    except socket.timeout as e:
        print(f"请求超时: {url}")
        return None
    return decode_data
