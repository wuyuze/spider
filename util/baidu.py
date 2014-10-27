__author__ = 'Administrator'
# coding=utf-8
import urllib

from bs4 import BeautifulSoup


url = 'http://www.baidu.com/s'
qzurl = 'http://www.jianshu.com/p/7699276a9158'
values = {'wd': '网球'}
encoded_param = urllib.urlencode(values)
full_url = url + '?' + encoded_param
response = urllib.urlopen(qzurl)
soup = BeautifulSoup(response)
alinks = soup.find_all('title')
print(soup.title)
print(alinks)
blinks = soup.find_all('div class="show-content"')

# print(soup.find())f.write(content.string)
# print(blinks)
content = soup.findAll(attrs={"class": "show-content"})
f = open(soup.title.string + '.txt', 'w')
cont = str(content[0])
f.write(cont)
f.close()
#print(content.div)
#print(soup.findAll('div',{'class':'show-content'}))

# print content
