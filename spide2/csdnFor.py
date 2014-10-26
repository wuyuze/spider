__author__ = 'Administrator'
import urllib2

from bs4 import BeautifulSoup



page = urllib2.urlopen('http://forum.csdn.net/SList/OL_Script//')
soup = BeautifulSoup(page)



for i in soup('td', style="word-break: break-all"):
    print i.a.string.encode('gb2312'), i.a['href']

