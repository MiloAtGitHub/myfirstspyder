# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import ExampleItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.chinacs.org.cn']
    start_urls = ['http://www.chinacs.org.cn/']

    def parse(self, response):

        pass
