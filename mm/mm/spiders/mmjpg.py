# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from mm.items import MmItem

class MmjpgSpider(scrapy.Spider):
    name = 'mmjpg' # 爬虫名
    allowed_domains = ['mmjpg.com'] # 可选，保证我们的爬虫只爬该域名下的网页
    base_url = 'http://www.mmjpg.com/home/'

    start_urls = [base_url + str(1)] # 修改到我们要使用的

    def parse(self, response):
        items = []

        infos = response.xpath("//div[@class='pic']//span/a") # 拿到所有需要的 a 标签
        for info in infos: # 遍历拿到的 a 标签 
            item = MmItem() # 每次循环都创建一个 MmItem 实例
            item['url'] = info.xpath("./@href").extract_first()
            item['title'] = info.xpath("./text()").extract_first()
            items.append(item) # 将 item 类字典类型放入列表

        for item in items: # 遍历列表发送所有的页面
            yield Request(item['url'], meta={'item':item}, callback=self.parse_img)

        if '下一页' in response.xpath("//div[@class='page']/a/text()").extract():
            url = 'http://www.mmjpg.com' + response.xpath("//div[@class='page']/a/@href").extract_first()
            yield Request(url, callback=self.parse)

    def parse_img(self, response):
        item = response.meta['item']
        
        item['url'] = response.xpath("//div[@id='content']//img/@src").extract_first()
        # print('+'*100)
        # print(item['url'])
        # print('+'*100)
        yield item

        next_page = response.xpath("//a[@class='ch next']")
        if next_page.xpath('./text()').extract_first() == '下一张':
            url = 'http://www.mmjpg.com'  + next_page.xpath('./@href').extract_first()
            yield Request(url,callback=self.parse_img, meta={'item':item})
        else:
            return