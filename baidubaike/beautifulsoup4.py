# coding=utf-8
import urllib2

import bs4;

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

url = "http://baike.baidu.com/view/42901.htm";

response = urllib2.urlopen(url)

soup = bs4.BeautifulSoup(html,'html.parser')
soup.find_all("")
# print response
# print soup.prettify()
print soup.find_all("a")[2]

