__author__ = 'Administrator'
import urllib2


def save(url):
    f = urllib2.urlopen(url)
    with open(url, "wb") as code:
        code.write(f.read())

def save(url, name):
    f = urllib2.urlopen(url)
    with open(name, "wb") as code:
        code.write(f.read())

