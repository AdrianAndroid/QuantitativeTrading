import requests

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'hq.sinajs.cn',
    'Referer': 'https://finance.sina.com.cn/realstock/company/sz002230/nc.shtml',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Storage-Access': 'active',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '0',
    'sec-ch-ua-platform': '"macOS"'
}

url = 'https://hq.sinajs.cn/list=sz002230'

# 使用requests库进行请求
response = requests.get(url, headers=headers, verify=False)
compressed_data = response.content
print('old data',compressed_data)

# 解压缩数据
# with gzip.GzipFile(fileobj=io.BytesIO(compressed_data)) as f:
#     decompressed_data = f.read()

# 打印解压缩后的数据
print(compressed_data.decode('gbk'))