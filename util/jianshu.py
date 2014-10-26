__author__ = 'Administrator'
import re
import urllib2
import os


def getPageURLs(url):
    text = urllib2.urlopen(url).read()
    pattern = r'<a href="(/p/.+)" target="_blank">'
    regex = re.compile(pattern)
    urlList = re.findall(regex, text)
    return urlList


def mkdir(filedir):
    if (not (os.path.exists(filedir))):
        os.mkdir(filedir)


def getStore(cnt, url):
    text = urllib2.urlopen('http://www.jianshu.com' + url)
    context = text.read()
    text.close()
    dirname = "jianshu"
    mkdir(dirname)
    filepath = os.getcwd() + os.sep + dirname + os.sep + str(cnt) + '.html'
    filename = 'hanhan/' + str(cnt) + '.html'
    f = open(filepath, 'w')
    f.write(context)
    f.close()


def getAllURLs():
    cnt = 0
    tmp = getPageURLs('http://www.jianshu.com/collection/48716610ce86')
    for i in tmp:
        cnt += 1
        getStore(cnt, i)


if __name__ == '__main__':
    getAllURLs()