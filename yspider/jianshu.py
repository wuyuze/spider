# encoding=gbk
import urllib
import re
import urllib2
import os

from bs4 import BeautifulSoup

from tools import getart


def getPageURLs(url):
    text = urllib2.urlopen(url).read()
    pattern = r'<a href="(/p/.+)" target="_blank">'
    regex = re.compile(pattern)
    urlList = re.findall(regex, text)
    return urlList


def mkdir(filedir):
    if (not (os.path.exists(filedir))):
        os.mkdir(filedir)


def getasay(url):
    cnt = 0
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)
    tmp = getPageURLs(url)
    for k in tmp[0:100]:
        cnt += 1
        getart.saveart(soup.title.string, 'http://www.jianshu.com' + k)
    # getStore('千变', cnt, k)


def getAllURLs():
    thousand = 'http://www.jianshu.com/collection/f16b3d483ec2?max_id=40472'
    fancy = 'http://www.jianshu.com/collection/6e34977b3711'
    poem = 'http://www.jianshu.com/collection/655e6db2abc7'
    # urlList = ['http://www.jianshu.com/collection/723de9bac3cd',
    # 'http://www.jianshu.com/collection/6e34977b3711',
    # 'http://www.jianshu.com/collection/655e6db2abc7']
    # 每天写一千字改变自己  怪东西 竹间诗筏
    # for i in urlList:
    getasay(thousand)
    #getasay(fancy)
    #getasay(poem)


if __name__ == '__main__':
    getAllURLs()