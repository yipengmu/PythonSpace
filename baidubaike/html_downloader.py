import urllib2


class HtmlDownloader(object):
    def __init__(self):
        super(HtmlDownloader, self).__init__()

    def download(self,url):
        if  url is None:
            return None

        response = urllib2.urlopen(url)

        # print "rep = " +  response.read()

        return response.read()