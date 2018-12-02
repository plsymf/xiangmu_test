# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position=scrapy.Field()
    salary=scrapy.Field()
    company=scrapy.Field()
    company_address=scrapy.Field()
    position_info=scrapy.Field()
    company_size=scrapy.Field()
    company_ip=scrapy.Field()
    company_nature=scrapy.Field()
    company_business=scrapy.Field()
    exp_require=scrapy.Field()
    edu_require=scrapy.Field()
    recruit_num=scrapy.Field()
