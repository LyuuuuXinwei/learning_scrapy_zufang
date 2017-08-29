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
    # 用scrapy.Field定义要爬取的元素:
    title = scrapy.Field()
    price = scrapy.Field()
    #设定好之后，ZufangItem的实例（ganji.py-zf）就只能有title.price两种key，
    pass
