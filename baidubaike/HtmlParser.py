#-*-coding:utf8-*-
import urllib
import urllib2

import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def get_new_urls(self,pageUrl,soup):
        if pageUrl is None:
            return None

        findout_new_urls = set()

        links = soup.find_all('a',href=re.compile(".htm"))

        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(pageUrl,new_url)
            print "new_url=" + new_url
            print "new_full_url=" + new_full_url
            findout_new_urls.add(new_full_url)
            return findout_new_urls

    def get_new_data(self,pageUrl,responseSoup):
        result = {}
        
        # url
        result['url'] = pageUrl

        # title
        result['title'] = responseSoup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1').get_text()

        # summary
        result['summary'] = responseSoup.find('div',class_='para').get_text()

        print result
        return result

    def start_parser(self,page_url,html_content):
        if page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content,'html.parser', from_encoding='utf-8')

        new_urls = self.get_new_urls(page_url,soup)
        new_data = self.get_new_data(page_url,soup)

        return new_urls,new_data

# url = "http://baike.baidu.com/view/42901.htm";
#
# response = urllib2.urlopen(url)
#
# responseSoup = BeautifulSoup(response,"html.parser")
#
# # print responseSoup.find_all(class_='lemma-summary')[0]
#
# title_node = responseSoup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
#
# print title_node.get_text()
# print responseSoup.prettify()