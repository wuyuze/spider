__author__ = 'Administrator'
# coding=utf-8
import urllib

from bs4 import BeautifulSoup


url = 'http://www.baidu.com/s'
qzurl = 'http://user.qzone.qq.com/462679107/4'
values = {'wd': '网球'}
encoded_param = urllib.urlencode(values)
full_url = url + '?' + encoded_param
response = urllib.urlopen(qzurl)
soup = BeautifulSoup(response)
alinks = soup.find_all('a')
print(alinks)