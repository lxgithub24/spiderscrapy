import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
#    allowed_domains = ["s.weibo.com/weibo/%25E7%25A6%258F%25E5%258E%259F%25E7%2588%25B1&nodup=1&page=1"]
 #   start_urls = [
  #      "http://s.weibo.com/weibo/%25E7%25A6%258F%25E5%258E%259F%25E7%2588%25B1&nodup=1&page=1/"
    #]

    allowed_domains = ["http://s.weibo.com/weibo/asdf&Refer=index"]
    start_urls = [
        "http://s.weibo.com/weibo/asdf&Refer=index"
    ]


    def parse(self, response):
        filename = "sinaweibo"
        with open(filename, 'wb') as f:
            f.write(response.body)

