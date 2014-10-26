__author__ = 'Administrator'
import re
import urllib2


def getPageURLs(url):
    text = urllib2.urlopen(url).read()
    pattern=r'<a href="(/p/.+)" target="_blank">'
   # pattern = r'<a title=".+" target="_blank" href="(http://blog.sina\.com\.cn.+\.html)">'
    regex = re.compile(pattern)
    urlList = re.findall(regex, text)
    print urlList
    return urlList


def getStore(cnt, url):
    text = urllib2.urlopen(url)
    context = text.read()
    text.close()
    filename = 'hanhan' + str(cnt) + '.html'
    f = open(filename, 'w')
    f.write(context)
    f.close()


def getAllURLs():
    urls = []
    cnt = 0
    for i in xrange(1, 8):
        urls.append('http://blog.sina.com.cn/s/articlelist_1191258123_0_' + str(i) + '.html')
 #   for url in urls:
        tmp = getPageURLs('http://www.jianshu.com/collection/48716610ce86')
        for i in tmp:
            cnt += 1
        #    getStore(cnt, i)


if __name__ == '__main__':
    getAllURLs()