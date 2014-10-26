__author__ = 'Administrator'
import urllib2
import cookielib


def save(url):
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    operate = opener.open(req)
    msg = operate.read()
    print(url)
    f = open(url, 'w')
    f.write(msg)
    f.close()


def save(url, name):
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    operate = opener.open(req)
    msg = operate.read()
    print(url)
    f = open(name + 'html', 'w')
    f.write(msg)
    f.close()


def save(url, name, text):
    cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    req = urllib2.Request(url)
    operate = opener.open(req)
    msg = operate.read()
    print(url)
    f = open(name + 'txt', 'w')
    f.write(msg)
    f.close()