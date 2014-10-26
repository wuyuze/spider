__author__ = 'Administrator'
import urllib2

url = 'http://www.baidu.com/s?wd=cloga'
content = urllib2.urlopen(url).read()

import re

urls_pat = re.compile(r'<span class="g">(.*?)</span>')
siteUrls = re.findall(urls_pat, content)

from bs4 import BeautifulSoup

soup=BeautifulSoup(content)
siteUrls = soup.findAll('span', attrs={'class': 'g'})
print(siteUrls)
