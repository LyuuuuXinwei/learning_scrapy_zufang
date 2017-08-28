# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ZufangPipeline(object):
    def open_spider(self,spider):
        self.conn=sqlite3.connect('zufang.sqlite')
        self.cur=self.conn.cursor()

    def process_item(self, item, spider):
        # print(spider.name,'pipelines')
        insert_sql="insert into z (title,price) values('{}','{}')".format(item['title'],item['price'])
        print(insert_sql)
        self.cur.execute(insert_sql)
        self.conn.commit()
        return item

    def spider_close(self,spider):
        self.conn.close()
