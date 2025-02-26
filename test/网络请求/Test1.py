# from urllib import request
# resp = request.urlopen("http://www.baidu.com")
# print(resp.read())

# from urllib import request
# request.urlretrieve('http://www.baidu.com/', 'baidu.html')


# 编码
# from urllib import parse
# data = {'name':'爬虫基础','greet':'hello world','age':100}
# qs = parse.urlencode(data)
# print(qs)

# from urllib import parse
# qs = "name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80&greet=hello+world&age=100"
# parse = parse.parse_qs(qs)
# print(parse)
# print(type(parse))