import scrapy


# from ..items import BossItem

class Boss(scrapy.Spider):
    name='boss'
    def start_requests(self):
        req = scrapy.Request(url='http://www.neitui.me/?name=job&handle=lists&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&page=1')
        # meta类字典结构  必须绑定到meta属性的proxy中
        req.meta['proxy'] = 'http://136.228.128.6:59680'
        yield req
    def parse(self, response):
        print(response.text)
        # print(response.xpath('//ul[@class="list-items"]/li').extract())



























    # def parse(self, response):
    #     # proxy=['http://45.76.78.152:1080','http://136.228.128.6:59680','http://203.187.169.101:80'
    #     #        ,'45.40.206.190:9999','111.75.223.9:30646','112.74.73.134:8088',
    #     #     '117.191.11.80:8080',
    #     #        '117.191.11.80:8080',
    #     #        '117.191.11.78:80',
    #     #        '113.108.242.36:47713'
    #     #        ]
    #     req = scrapy.Request(self.start_urls)
    #     # meta类字典结构  必须绑定到meta属性的proxy中
    #     req.meta['proxy'] = 'http://136.228.128.6:59680'
    #     yield req
    #     print(response.xpath('//ul[@class="list-items"]/li'))
    #     # url_details=[]
    #     # for url_detail in response.xpath('//ul[@class="list-items"]/li'):
    #     #     url_details.append(url_detail.xpath('//div[@class="mt5 clearfix"]/a/@href'))
    #     #     print(url_detail.xpath('//div[@class="mt5 clearfix"]/a/@href','this is url'))
    #     # if url_details:
    #     #     yield scrapy.Request(url_details.pop())
    # # def parse1(self,resp):
    # #     item=BossItem()
    # #     #获取详情页的数据
    # #     item['position']=resp.xpath('').extract()
    # #     # print(item['position'],'this is item["position"]')
    # #     yield item