import os
import urllib
import re

from bs4 import BeautifulSoup


__author__ = 'Administrator'


def saveart(dir, url):
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)

    ssss = '<title>一个关于什么的故事</title>'
    reg = re.compile(r'.+?>(.+?)</.+?')
    stra = reg.findall(ssss)
    print(stra[0])

    ss = ssss.replace("</title>", "").replace("<title>", "")
    print(ss)

    blinks = soup.find_all('div class="show-content"')  # print(soup.find())f.write(content.string)
    # print(blinks)

    mkdir(dir)
    strs = soup.findAll(name='p', attrs={'class': 'show-content"'})
    content = soup.findAll(attrs={"class": "show-content"})

    filepath = os.getcwd() + os.sep + dir + os.sep + soup.title.string
    f = open(r'' + filepath + '.htm', 'w')
    cont = str(content[0])
    f.write(cont)
    f.close()


def mkdir(filedir):
    if (not (os.path.exists(filedir))):
        os.mkdir(filedir)
