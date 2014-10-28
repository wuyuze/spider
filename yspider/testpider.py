# encoding=utf8
import sys

__author__ = 'Administrator'
from tools import Spider

if __name__ == '__main__':
    reload(sys)
    i = range(5, 11, 1)
    for l in i:
        print str(l)
        sp = Spider.spider("http://zyxs0418.lofter.com/?page=" + str(l))
        sp.seti(l)
        sp.getpageurls(r'<img src="(.+)">')
        sp.savajpg()