__author__ = 'Administrator'
# coding:utf-8
import re
import urllib2

from bs4 import BeautifulSoup


def getPageURLs(url):
    text = urllib2.urlopen(url).read()
    pattern = r'<a title=".+" target="_blank" href="(http://blog.sina\.com\.cn.+\.html)">'
    regex = re.compile(pattern)
    urlList = re.findall(regex, text)
    return urlList


def getStore(title, url):
    text = urllib2.urlopen(url)
    context = text.read();
    text.close()
    filename = 'HanhanArticle/' + title + '.html'
    f = open(filename, 'w')
    f.write(context)
    f.close()


def getTitle(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    title = soup.find('title')
    string = str(title)
    return string[7: -28]


def Judge(title):
    lens = len(title)
    for i in xrange(0, lens):
        if title[i] == '*':
            return False
    return True


def getAllURLs():
    urls = []
    for i in xrange(1, 8):
        urls.append('http://blog.sina.com.cn/s/articlelist_1191258123_0_' + str(i) + '.html')
    for url in urls:
        tmp = getPageURLs(url)
        for i in tmp:
            title = getTitle(i).decode('utf-8')
            print title
            if title[0] != '.' and Judge(title):
                getStore(title, i)


if __name__ == '__main__':
    getAllURLs()