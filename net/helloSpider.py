import urllib2,cookielib

url = "http://www.baidu.com";

reponse1 = urllib2.urlopen(url)

print reponse1.getcode();


print "start by cookies ....";
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
reponseByCookie = urllib2.urlopen(url)

print reponseByCookie.getcode()
print reponseByCookie.read()