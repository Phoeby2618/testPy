import urllib.request
import http.cookiejar

#1. 最简单使用urlopen来接受链接
response1=urllib.request.urlopen("http://baidu.com")
print(response1.read())

# 2.使用request来接收参数
req=urllib.request.Request("http://baidu.com")
response2=urllib.request.urlopen(req)
print(response2.read())

# 2.1添加头部信息
req=urllib.request.Request("http://baidu.com")
req.add_header('User-Agent','Mozilla/5.0')
response3=urllib.request.urlopen(req)
print(response3.read())

# 3.增加cookie容器
cookie=http.cookiejar.CookieJar()
openner=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
# 建立一个open容器处理cookie，打开url
response4=openner.open("http://baidu.com")
print(response4.read())

# 测试beautifulsoup4
import bs4
print(bs4)