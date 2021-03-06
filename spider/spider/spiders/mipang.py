# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import  Rule
 
from spider.items import SpiderItem
 
 
 
 
class MipangSpider(scrapy.Spider):
    name = "mipang"
    allowed_domains = ["maps.mipang.com"]
    start_urls = ["http://maps.mipang.com/", ]
 
    rules = (
        Rule(LinkExtractor(allow=r'start=\d{1,3}$'), callback='parse_item', follow=True),
    )
 
    def parse(self, response):
        items = []
        province_list = response.css('div.box.modbox.mod-weather-list h4')
        filename = "province"
        for province in province_list:
            item = SpiderItem()
            item['provincename'] = province.xpath('a/text()').extract()[0]
            print "################################################"
            print filename
            with open(filename, 'ab') as f:
                print "################################################"
                f.write(province.xpath('a/text()').extract()[0]+'\n')

