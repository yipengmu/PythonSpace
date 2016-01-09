#-*-coding:utf8-*-
from baidubaike.SpiderBaike import SpiderBaike


if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderBaike()
    obj_spider.craw(root_url)