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


def getStore(dir, cnt, url):
    text = urllib2.urlopen('http://www.jianshu.com' + url)
    context = text.read()

    text.close()
    mkdir(dir)
    filepath = os.getcwd() + os.sep + dir + os.sep + str(cnt) + '.html'
    filename = 'hanhan/' + str(cnt) + '.html'
    f = open(filepath, 'w')
    f.write(context)
    f.close()


def getasay(url):
    cnt = 0
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)
    tmp = getPageURLs(url)
    for k in tmp[0:100]:
        cnt += 1
        getart.saveart(soup.title.string, 'http://www.jianshu.com' + k)
        # getStore('ǧ��', cnt, k)


def filter_tags(htmlstr):
    # �ȹ���CDATA
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # ƥ��CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
    re_br = re.compile('<br\s*?/?>')  # ������
    re_h = re.compile('</?\w+[^>]*>')  # HTML��ǩ
    re_comment = re.compile('<!--[^>]*-->')  # HTMLע��
    s = re_cdata.sub('', htmlstr)  # ȥ��CDATA
    s = re_script.sub('', s)  # ȥ��SCRIPT
    s = re_style.sub('', s)  # ȥ��style
    s = re_br.sub('\n', s)  # ��brת��Ϊ����
    s = re_h.sub('', s)  # ȥ��HTML ��ǩ
    s = re_comment.sub('', s)  # ȥ��HTMLע��
    # ȥ������Ŀ���
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    return s


def getAllURLs():
    thousand = 'http://www.jianshu.com/collection/723de9bac3cd'
    fancy = 'http://www.jianshu.com/collection/6e34977b3711'
    poem = 'http://www.jianshu.com/collection/655e6db2abc7'
    # urlList = ['http://www.jianshu.com/collection/723de9bac3cd',
    # 'http://www.jianshu.com/collection/6e34977b3711',
    # 'http://www.jianshu.com/collection/655e6db2abc7']
    # ÿ��дһǧ�ָı��Լ�  �ֶ��� ���ʫ��
    # for i in urlList:
    tem = getPageURLs("http://lmomol.lofter.com/")
    k = 0
    for i in tem:
        k += 1
        savefile.save(i, str(k) + '.jpg')


if __name__ == '__main__':
    getAllURLs()