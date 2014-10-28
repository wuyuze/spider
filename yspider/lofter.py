# encoding=gbk
import urllib
import re
import urllib2
import os

from bs4 import BeautifulSoup

from tools import getart, savefile


def getPageURLs(url):
    text = urllib2.urlopen(url).read()
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)
    alinks = soup.find_all('title')
    blinks = soup.find_all('img')
    pattern = r'<a href="(/p/.+)" target="_blank">'
    pattern = r'<img src="(.+)" />'

    regex = re.compile(pattern)
    urlList = re.findall(regex, text)
    print(urlList)
    return urlList


def mkdir(filedir):
    if (not (os.path.exists(filedir))):
        os.mkdir(filedir)

def filter_tags(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # 处理换行
    re_h = re.compile('</?\w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('\n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    # 去掉多余的空行
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    return s


def getAllURLs():
    tem = getPageURLs("http://lmomol.lofter.com/")
    k = 0
    for i in tem:
        k += 1
        savefile.save(i, str(k) + '.jpg')


if __name__ == '__main__':
    getAllURLs()