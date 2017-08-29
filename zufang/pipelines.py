# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
'''
pipelines接收到Item并通过它执行一些行为，同时也决定此Item是否继续通过pipeline，或是被丢弃而不再进行处理
以下是item pipeline的一些典型应用：

清理HTML数据
验证爬取的数据(检查item包含某些字段)
查重(并丢弃)
将爬取结果保存到数据库中

启动pipeline需要在setting中找到 ITEM_PIPELINES 配置，几个class有几个
'''
class ZufangPipeline(object):

    def open_spider(self,spider):
        '''当spider被开启时，这个方法被调用'''
        self.conn=sqlite3.connect('zufang.sqlite')
        self.cur=self.conn.cursor()

    def process_item(self, item, spider):
        '''
        process_item是必须实现的方法
        这个方法必须返回一个具有数据的dict，或是Item或任何继承类对象，或是抛出 DropItem 异常，被丢弃的item将不会被之后的pipeline组件所处理
        '''
        # print(spider.name,'pipelines')
        insert_sql="insert into z (title,price) values('{}','{}')".format(item['title'],item['price'])
        print(insert_sql)
        self.cur.execute(insert_sql)
        self.conn.commit()
        return item

    def spider_close(self,spider):
        '''当spider被关闭时，这个方法被调用'''
        self.conn.close()

    '''
    一个清理数据的例子

    def process_item(self, item, spider):
        if item['price']:
            if item['price_excludes_vat']:
                item['price'] = item['price'] * self.vat_factor
            return item
        else:
            raise DropItem("Missing price in %s" % item)
    '''

    '''
    一个写入json文件的例子
    
    class JsonWriterPipeline(object):
    
        def __init__(self):
            self.file = open('items.jl', 'wb')
    
        def process_item(self, item, spider):
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item
    '''
    #利用__init__初始化数据库/新建空白写入文件，上例是用open_spider，是否用init时要考虑传参问题啊，那还是open_spider比较好
    '''
    一个用pymongo写入mongodb的例子
    '''
    class MongoPipeline(object):
    
        collection_name = 'scrapy_items'
    
        def __init__(self, mongo_uri, mongo_db):
            self.mongo_uri = mongo_uri
            self.mongo_db = mongo_db
    
        @classmethod #TODO:from_crawler的用法
        def from_crawler(cls, crawler):
            return cls(
                mongo_uri=crawler.settings.get('MONGO_URI'),
                mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
            )
    
        def open_spider(self, spider):
            self.client = pymongo.MongoClient(self.mongo_uri)
            self.db = self.client[self.mongo_db]
    
        def close_spider(self, spider):
            self.client.close()
    
        def process_item(self, item, spider):
            self.db[self.collection_name].insert(dict(item))
            return item
    '''