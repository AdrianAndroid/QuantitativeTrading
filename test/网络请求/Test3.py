from urllib import request
import gzip
import io
import ssl

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
# }
# req = request.Request("https://www.baidu.com/",headers=headers)
# resp = request.urlopen(req)
# print(resp.read())

# headers = {
#     'accept':'*/*',
#     'accept-encoding':'gzip, deflate, br, zstd',
#     'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'connection':'keep-alive',
#     'host':'hq.sinajs.cn',
#     'referer':'https://finance.sina.com.cn/stock/',
#     'sec-ch-ua':'"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133",'
#     'sec-ch-ua-mobile':?0,
#     'sec-ch-ua-platform':'"macOS"',
#     'sec-fetch-dest':'script',
#     'sec-fetch-mode':'no-cors',
#     'sec-fetch-site':'cross-site',
#     'sec-fetch-storage-access':'active',
#     'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
# }

# headers = {
#     'accept': '*/*',
#     'accept-encoding': 'gzip, deflate, br, zstd',
#     'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'connection': 'keep-alive',
#     'host': 'hq.sinajs.cn',
#     'referer': 'https://finance.sina.com.cn/stock/',
#     'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133",',
#     'sec-ch-ua-mobile': '0',  # 将?0替换为字符串'0'或布尔值False
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'script',
#     'sec-fetch-mode': 'no-cors',
#     'sec-fetch-site': 'cross-site',
#     'sec-fetch-storage-access': 'active',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
# }
# url = r'https://hq.sinajs.cn/rn=1740488751907&list=s_sh000001,s_sz399001,s_sh000300,s_bj899050,s_sz399006'
# req = request.Request(url,headers=headers)
# # req = request.Request(url,headers=headers, data=parse.urlencode(data), method='POST)
# resp = request.urlopen(req)
# compressed_data = resp.read()
# print(compressed_data)
# with gzip.GzipFile(fileobj=io.BytesIO(compressed_data)) as f: 
#     decompressed_data = f.read()
# # 打印解压缩后的数据
# print(decompressed_data.decode('gbk'))



# import gzip
# import io
# compressed_data = b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03u\x90MJCA\x0c\x80\xf7\x9eB\xde:o\xc8\xcfd\x92 =K\xd1Uqg+]x\x9e\xe2\xba\xc5\n\x05OP7\x82\x8bw\x03\xb7\xbd\x81`\xa6\xaeT\x9cMBH\xbe|\x99\xf5\xf5\xf2rq7_\xdd/\xe7\xab\xf9j\x81\xfd\xd1l8\xbeM\x9b\xe9\xf0\xfa\t"\xb5\x15\x94p\x18\xb9\x95p\xcb\x04\x8b#(\x9b\x9a+XF\x0c\xb3\xe1\xeab\xfd\x83\xf5 \x11\xdf\xac\xd3\xb4y:N\x07 t\xadE\x11Fb/Z\x13E\x85\x0c\x9c\xd8\x02k\xab@\xd4\x82\x95Y\xfe\xd0\xba\x99 \xce\x86\x97\xc7\xe3)\x13\x90l,MQa\xac\xb5`\xcb\xe9N# \xf3\xbe\x08\xc4,\x9c\xaa\xfeF\xdd\xdcz\x8ai\xa2v\xbbi\x936$i\xc3\xd2\xe7\xbd\xb8j\xe7T<\xd7\xb5\x19\x1a;p\xa0\xd7\x16M\x82J\x8a\xfcsk\x9b\r\xfb\xfd\xfb\xf3\xf6#oe\xaeX4\xf2\xd7\xbae;\xbb\t\x88\x9bT\r\x03\xaa\x9c\x92g\xd2\x17uEk\xa9\x82\x01\x00\x00'
# # 解压缩数据
# with gzip.GzipFile(fileobj=io.BytesIO(compressed_data)) as f:
#     decompressed_data = f.read()
# # 打印解压缩后的数据
# print(decompressed_data.decode('gbk'))


# headers = {
#     'accept': '*/*',
#     'accept-encoding': 'gzip, deflate, br, zstd',
#     'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'connection': 'keep-alive',
#     'host': 'hq.sinajs.cn',
#     'referer': 'https://finance.sina.com.cn/realstock/company/sz002230/nc.shtml',
#     'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
#     'sec-ch-ua-mobile': '0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'script',
#     'sec-fetch-mode': 'no-cors',
#     'sec-fetch-site': 'cross-site',
#     'sec-fetch-storage-access': 'active',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
# }
# url = r'https://hq.sinajs.cn/list=sz002230'
# # req = request.Request(url,headers=headers)
# # resp = request.urlopen(req)
# # compressed_data = resp.read()
# # print(compressed_data)
# # with gzip.GzipFile(fileobj=io.BytesIO(compressed_data)) as f: 
# #     decompressed_data = f.read()
# # # 打印解压缩后的数据
# # print(decompressed_data.decode('gbk'))
# # 创建一个不验证SSL证书的上下文
# context = ssl._create_unverified_context()
# # 使用不验证SSL证书的上下文进行请求
# req = request.Request(url, headers=headers)
# resp = request.urlopen(req, context=context)
# compressed_data = resp.read()
# print(compressed_data)
# with gzip.GzipFile(fileobj=io.BytesIO(compressed_data)) as f: 
#     decompressed_data = f.read()
# # 打印解压缩后的数据
# print(decompressed_data.decode('gbk'))


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