from urllib import request

resp = request.urlopen("http://httpbin.org/ip")
print(resp.read().decode("utf-8"))

# handler = request.ProxyHandler({"http":"119.3.113.151:9094"})
handler = request.ProxyHandler({"http":"118.113.244.222:2324"})
opener = request.build_opener(handler)
req = request.Request("http://httpbin.org/ip")
resp = opener.open(req)
print(resp.read().decode("utf-8"))