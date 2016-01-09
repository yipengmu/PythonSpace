import cookielib
import urllib2

url = "http://www.baidu.com";


reponse = urllib2.urlopen(url)

print reponse.getcode();


print "start by cookies ....";
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
reponseByCookie = urllib2.urlopen(url)



print reponseByCookie.getcode()
print reponseByCookie.read()