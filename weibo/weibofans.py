# coding=utf-8
import cookielib
import urllib2
import bs4;


url = "http://weibo.com/1310602621/fans?rightmod=1&wvr=6";

# add cookies
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

header = { 'Connection' : 'keep-alive',    'cookie' : "",   'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'  }

req = urllib2.Request(url, headers=header)

response = urllib2.urlopen(req)

supp = bs4.BeautifulSoup(response,"html.parser")



print supp.prettify()