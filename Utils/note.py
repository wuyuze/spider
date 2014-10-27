__author__ = 'Administrator'


def saveart(dir, url):
    response = urllib.urlopen(url)
    soup = BeautifulSoup(response)
    alinks = soup.find_all('title')
    print(soup.title)
    print(alinks)
    blinks = soup.find_all('div class="show-content"')  # print(soup.find())f.write(content.string)
    # print(blinks)
    mkdir(dir)
    content = soup.findAll(attrs={"class": "show-content"})
    filepath = os.getcwd() + os.sep + dir + os.sep + soup.title.string
    f = open(filepath + '.htm', 'w')
    cont = str(content[0])
    f.write(cont)
    f.close()
    input_file = codecs.open(filepath + '.htm', mode="r", encoding="utf8")
    text = input_file.read()
    html = markdown(text)
    # print
    print html
    # Write string html to disk
    output_file = codecs.open(filepath + '.html', mode="w", encoding="utf8")
    output_file.write(html)
    output_file.close()

