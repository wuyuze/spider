__author__ = 'Administrator'
import urllib2

from bs4 import BeautifulSoup


class GrabHtml(object):
    def __init__(self, url):
        self.url = url

    def grab_html(self):
        req = urllib2.Request(self.url)
        con = urllib2.urlopen(req)
        soup = BeautifulSoup(con.read())
        con.close()
        return soup


if __name__ == "__main__":
    url = 'http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000'
    obj = GrabHtml(url)
    soup = obj.grab_html()
    content = soup.findAll('div', id='main')

    print content