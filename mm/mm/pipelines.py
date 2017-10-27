# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from .settings import IMAGES_STORE as imgs_store
from scrapy.pipelines.images import ImagesPipeline

class MmPipeline(ImagesPipeline):   # 因为下图像，所以可以继承 ImagesPipeline
    def get_media_requests(self, item, info):
        url = item['url'] 
        # print('-'*90)
        # print(dir(info.spider.start_urls[0]))
        # print('-'*90)
        # return
        headers={'Referer':info.spider.start_urls[0]}
        yield scrapy.Request(url, headers=headers)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        # if not image_paths:
        # raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        # return item
        if not os.path.exists(imgs_store+item['title']):
            os.mkdir(imgs_store+item['title'])
        os.rename(imgs_store+image_paths[0], imgs_store+item['title']+'/'+item['url'].split('/')[-1])
        # print(image_paths)
        # print(imgs_store)