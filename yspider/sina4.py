__author__ = 'Administrator'
# encoding:utf-8
import urllib2
import os
import re

from bs4 import BeautifulSoup


def geturl(url):
    for k in url:
        text = urllib2.urlopen(k).read()
    print(text)
    pattern = 'http://blog.sina.com.cn/s/blog_\S+.html'
    regex = re.compile(pattern)
    urllist = regex.findall(text.decode("utf-8"))
    for i in urllist:
        print(i)
        getAllList(i)


def mkdir(filedir):
    if (not (os.path.exists(filedir))):
        os.mkdir(filedir)


def getAllList(url):
    dirname = 'chapiter'
    mkdir(dirname)
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content.decode("utf-8").replace(r'\xa0', ' '))
    print(soup.title.string)
    # filename = i[7:-8]
    #  filepath = os.getcwd() + os.sep + dirname + os.sep + filename + '.html'
    #f = open(filepath, 'wb')
    #f.write(content)
    #f.close()


def getAllArticle():
    url = []
    for i in range(1, 8):
        url.append('http://blog.sina.com.cn/s/articlelist_1191258123_0_' + str(i) + '.html')
        geturl(url)


if __name__ == '__main__':
    getAllArticle()