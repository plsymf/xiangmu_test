import scrapy
from lagou.lagou.items import LagouItem
class Boss(scrapy.Spider):
    name='boss'
    start_urls='http://www.neitui.me/?name=job&handle=lists&keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE&page=1'
    def parse(self, response):
        yield scrapy.Request(self.start_urls)
        url_details=[]
        for url_detail in response.xpath('//ul[@class="list-items"]/li'):
            url_details.append(url_detail.xpath('//div[@class="mt5 clearfix"]/a/@href'))
        if url_details:
            yield scrapy.Request(url_details.pop(),callback=self.parse1)
    def parse1(self,resp):
        item=LagouItem()
        #获取详情页的数据
        item['']=resp.xpath('').extract()
        yield item