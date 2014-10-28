# encoding=utf8
import os
import urllib2
import re

from bs4 import BeautifulSoup


class spider():
    def __init__(self, urs):
        self.url = urs
        self.dir = ""
        self.urllist = []
        self.i = 1


    def seturl(self, urls):
        self.url = urls

    def seti(self, i):
        self.i = len(self.urllist) * (
            i - 1) + 1

    def getpageurls(self, regular):
        html = urllib2.urlopen(self.url).read()
        regx = re.compile(regular)
        soup = BeautifulSoup(html)
        self.dir = soup.title.string
        try:
            self.mkdir(self.dir)
        except:
            self.setdir('顺妞的旅行笔记')
        self.urllist = re.findall(regx, html)
        print(len(self.urllist))
        print(self.urllist)
        return self.urllist

    def setdir(self, di):
        self.dir = di
        self.mkdir(str(dir))

    # example
    # pattern = r'<a href="(/p/.+)" target="_blank">'
    # pattern = r'<img src="(.+)" />'

    def savajpg(self):
        for i in self.urllist:
            filepath = os.getcwd() + os.sep + self.dir + os.sep + str(self.i) + '.jpg'
            self.i += 1
            f = urllib2.urlopen(i)
            with open(filepath, "wb") as code:
                code.write(f.read())

    def savafile(self, formt):
        filepath = os.getcwd() + os.sep + self.dir + os.sep + str(self.i) + '.' + formt
        with open(filepath, "wb") as code:
            code.write(self.urllist)

    def savalink(self):
        for i in self.urllistp[1:]:
            print(str(self.i) + i)
            self.i += 1
            filepath = os.getcwd() + os.sep + self.dir + os.sep + str(self.i)
            f = urllib2.urlopen(i)
            with open(filepath, "wb") as code:
                code.write(f.read())

    def mkdir(self, filedir):
        if (not (os.path.exists(filedir))):
            print(filedir)
            os.mkdir(filedir)
