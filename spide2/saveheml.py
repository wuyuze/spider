__author__ = 'Administrator'
import urllib2
import cookielib

url = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'
cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

req = urllib2.Request(url)

operate = opener.open(req)
msg = operate.read()
print(msg)

f = open(url, 'w')
f.write(msg)
f.close()
