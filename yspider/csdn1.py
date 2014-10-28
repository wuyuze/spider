__author__ = 'Administrator'
# encoding:utf-8
import urllib2


def getURL(str):
    start = str.find(r'href=')
    start += 6
    end = str.find(r'.html')
    end += 5
    url = str[start: end]
    return url


def getContext(url):
    text = urllib2.urlopen(url).read()
    return text


def StoreContext(url):
    content = getContext(url)
    filename = url[-20:]
    open(filename, 'w').write(content)


if __name__ == '__main__':
    str = '<span class="atc_title"><a title="东望洋" target="_blank" href="http://blog.sina.com.cn/s/blog_4701280b0102eck1.html">东望洋</a></span>'
    url = getURL(str)
    StoreContext(url)
