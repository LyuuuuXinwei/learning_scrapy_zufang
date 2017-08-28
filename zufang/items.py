# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy #导入scrapy
'''
Item 是保存爬取到的数据的容器
'''

class ZufangItem(scrapy.Item): #新建scrapy.Item的类
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    pass
