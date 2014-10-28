# encoding=utf8
import urllib
import re
import urllib2
import os
import sys

from bs4 import BeautifulSoup


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
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)
    tmp = getPageURLs(url)
    for k in tmp:
        saveart(soup.title.string, 'http://www.jianshu.com' + k)
        # getStore('千变', cnt, k)


def getAllURLs():
    thousand = 'http://www.jianshu.com/collection/2mvgxp?max_id='
    a = range(10000, 20000, 1000)
    print(a)
    for i in a:
        getasay(thousand+str(i))
    fancy = 'http://www.jianshu.com/collection/6e34977b3711'
    poem = 'http://www.jianshu.com/collection/655e6db2abc7'
    # for i in list:
    # getasay(i)
    # urlList = ['http://www.jianshu.com/collection/723de9bac3cd',
    # 'http://www.jianshu.com/collection/6e34977b3711',
    # 'http://www.jianshu.com/collection/655e6db2abc7']
    # 每天写一千字改变自己  怪东西 竹间诗筏
    # for i in urlList:
    # getasay(fancy)
    # getasay(poem)


def saveart(dir, url):
    response = urllib.urlopen(url)

    soup = BeautifulSoup(response)
    alinks = soup.find_all('title')
    # print(soup.title)
    sss = soup.title.string
    # print(sss)
    ssss = '<title>一个关于什么的故事</title>'
    reg = re.compile(r'.+?>(.+?)</.+?')
    stra = reg.findall(ssss)
    #print(stra[0])
    ss = soup.title.string.replace("</title>", "").replace("<title>", "")
    # print(ss)
    # print(alinks)
    blinks = soup.find_all('div class="show-content"')  # print(soup.find())f.write(content.string)
    # print(blinks)
    mkdir(dir)
    strs = soup.findAll(name='p', attrs={'class': 'show-content"'})

    content = soup.findAll(attrs={"class": "show-content"})

    filepath = os.getcwd() + os.sep + dir + os.sep + soup.title.string
    print(url)
    print filepath
    f = open(r''+filepath + '.htm', 'w')
    cont = str(content[0])
    f.write(cont)
    f.close()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    getAllURLs()