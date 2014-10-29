# encoding=utf8
import codecs
import urllib
import re
import urllib2
import os
import sys

from bs4 import BeautifulSoup
from markdown import markdown

from soup.mark import Html2MarkdownParser


def mkdir(filedir):
    if (not (os.path.exists(filedir))):
        os.mkdir(filedir)


def getasay(url):
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)
    tmp = getPageURLs(url)
    for k in tmp:
        saveart(soup.title.string, 'http://www.jianshu.com' + k)


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
    arc = content[0]
    title = soup.findAll('title')
    filepath = os.getcwd() + os.sep + dir + os.sep + soup.title.string
    f = open(r'' + filepath + '.htm', 'w')
    cont = str(content[0])
    f.writelines(cont)
    f.close()

    input_file = codecs.open(filepath + '.htm', mode="r", encoding="utf8")
    text = input_file.read()
    html = markdown(text)

    output_file = codecs.open(filepath + '.html', mode="w", encoding="utf8")
    output_file.write(html)
    output_file.close()

    p = Html2MarkdownParser()
    p.feed(text)
    print(text)
    output_file = codecs.open(filepath + '.markdown', mode="w", encoding="utf8")
    output_file.write("# " + soup.title.text + p.get_markdown())
    print(p.get_markdown())
    p.close()
    # print p.get_markdown()


def start():
    thousand = 'http://www.jianshu.com/collection/f16b3d483ec2?max_id='
    a = range(16, 17, 1)
    # for i in a:
    # print(i)
    # getasay(thousand + str(i * 900))
    saveart('mark', 'http://www.jianshu.com/p/6d42ad6368fd')


if __name__ == '__main__':
    reload(sys)
    start()