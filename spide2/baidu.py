__author__ = 'Administrator'
import urllib2


def getStore(title, url):
    text = urllib2.urlopen(url)
    context = text.read();
    text.close()
    filename = '1.html'
    f = open(filename, 'w')
    f.write(context)
    f.close()


response = urllib2.urlopen('http://www.baidu.com/')
html = response.read()
getStore('baidu', 'http://www.baidu.com/')
