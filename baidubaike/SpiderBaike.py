import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from baidubaike import html_downloader
from baidubaike import html_outputer
from baidubaike import url_manager
from baidubaike.HtmlParser import HtmlParser


class SpiderBaike(object):

    def __init__(self):
        super(SpiderBaike, self).__init__()
        print 'start SpiderBaike ....'
        print 'start UrlManager ....'
        self.urls = url_manager.UrlManager()
        print 'start HtmlDownloader ....'
        self.downloader = html_downloader.HtmlDownloader()
        print 'start HtmlParser ....'
        self.hParser = HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        print 'start add_new_url ....'
        while self.urls.has_new_url():
            try:

                print 'start craw ....'
                # print("craw %d : %s" %(count, new_url))
                new_url = self.urls.get_new_url()

                print 'start download .... new_url= ' + new_url
                # print("craw %d : %s" %(count, new_url))

                html_cont = self.downloader.download(new_url)

                # print "result = " + html_cont
                new_urls, new_data = self.hParser.start_parser(new_url, html_cont)

                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)


                if count == 200:
                    break
                count = count + 1
            except Exception,ex:
                print('craw failed ' + ex)

        self.outputer.output_html()
