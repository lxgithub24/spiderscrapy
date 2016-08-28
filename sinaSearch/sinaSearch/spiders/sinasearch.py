# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import  Rule

from sinaSearch.items import SinasearchItem

class SinasearchSpider(scrapy.Spider):
    name = "sinasearch"
    allowed_domains = ["s.weibo.com/weibo/%25E7%25A6%258F%25E5%258E%259F%25E7%2588%25B1&nodup=1&page=1"]
    start_urls = (
        'http://s.weibo.com/weibo/%25E7%25A6%258F%25E5%258E%259F%25E7%2588%25B1&nodup=1&page=1/',
    )
    
#    rules = (
#        Rule(LinkExtractor(allow=r'start=\d{1,3}$'), callback='parse_item', follow=True),
#    )

    def parse(self, response):
        weibo_list = response.css('div.feed_list.W_texta div').encode('utf-8')
        filename = "username"
        for weibo in weibo_list:
            item = SinasearchItem()
            item['username'] = weibo.xpath('div/text()').xpath('string(.)').extract()[0]
            with open(filename, 'ab') as f:
                print "################################################"
                f.write(item['username']+'\n')
#             item['weibocontent'] = weibo.xpath('h4/a/text()').extract()[0]
#             item['posttime'] = weibo.xpath('h4/a/text()').extract()[0]
#             item['repostcount'] = weibo.xpath('h4/a/text()').extract()[0]
#             item['commentcount'] = weibo.xpath('h4/a/text()').extract()[0]
#             item['supportcount'] = weibo.xpath('h4/a/text()').extract()[0]

