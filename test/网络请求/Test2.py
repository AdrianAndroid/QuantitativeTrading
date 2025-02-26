from urllib import request,parse

url = 'http://www.baidu.com/aaa/bbbb/s;hello?username=zhiliao&t1=t1&t2=t2'

print('urlsplit:')
result = parse.urlsplit(url)
print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('query:',result.query)

print('分割线=======')

print('urlparse:')
result = parse.urlparse(url)
print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('query:',result.query)