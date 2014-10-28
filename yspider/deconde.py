# encoding=utf8
import codecs
import urllib
import re
import urllib2
import os
import sys

from bs4 import BeautifulSoup
from markdown import markdown


def mkdir(filedir):
    if (not (os.path.exists(filedir))):
        os.mkdir(filedir)


def getasay(url):
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)
    tmp = getPageURLs(url)
    for k in tmp:
        try:
            saveart(soup.title.string, 'http://www.jianshu.com' + k)
        except:
            print('error')


def getPageURLs(url):
    text = urllib2.urlopen(url).read()
    pattern = r'<a href="(/p/.+)" target="_blank">'
    regex = re.compile(pattern)
    urlList = re.findall(regex, text)
    return urlList


def saveart(dir, url):
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)
    mkdir(dir)
    content = soup.findAll(attrs={"class": "show-content"})
    title = soup.findAll(attrs={"class": "article"})
    filepath = os.getcwd() + os.sep + dir + os.sep + soup.title.string
    print(url)
    print filepath
    f = open(r'' + filepath + '.htm', 'w')
    cont = str(title[0])
    f.write(cont)
    f.close()
    input_file = codecs.open(filepath + '.htm', mode="r", encoding="utf8")
    text = input_file.read()
    html = markdown(text)
    # print
    print html
    # Write string html to disk
    output_file = codecs.open(filepath + '.html', mode="w", encoding="utf8")
    output_file.write(html)
    output_file.close()



def start():
    thousand = 'http://www.jianshu.com/collection/f16b3d483ec2?max_id='
    a = range(16, 64, 1)
    for i in a:
        print(i)
        getasay(thousand + str(i * 900))


if __name__ == '__main__':
    reload(sys)
    start()