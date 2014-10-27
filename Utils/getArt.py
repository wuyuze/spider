# coding=gbk
import os
import urllib
from bs4 import BeautifulSoup
from markdown import markdown
import codecs

def saveart(url):
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)
    alinks = soup.find_all('title')
    content = soup.findAll(attrs={"class": "show-content"})
    print(soup.title)
    print(alinks)
    blinks = soup.find_all('div class="show-content"')  # print(soup.find())f.write(content.string)
    # print(blinks)

    f = open(soup.title.string + '.txt', 'w')
    cont = str(content[0])
    f.write(cont)
    f.close()


def saveart(dir, url):
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)
    alinks = soup.find_all('title')
    print(soup.title)
    # print(alinks)
    blinks = soup.find_all('div class="show-content"')  # print(soup.find())f.write(content.string)
    # print(blinks)
    mkdir(dir)
    content = soup.findAll(attrs={"class": "show-content"})
    filepath = os.getcwd() + os.sep + dir + os.sep + soup.title.string
    f = open(filepath + '.htm', 'w')
    cont = str(content[0])
    f.write(cont)
    f.close()




def mkdir(filedir):
    if (not (os.path.exists(filedir))):
        os.mkdir(filedir)

# print(content.div)
# print(soup.findAll('div',{'class':'show-content'}))
# print content
