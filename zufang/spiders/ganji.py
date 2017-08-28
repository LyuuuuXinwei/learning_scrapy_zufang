import scrapy
from ..items import ZufangItem

class GanjiSpider(scrapy.Spider):
    name = 'zufang' #必创
    start_urls = ['http://bj.ganji.com/fang1/']

    def parse(self, response):
        print(response)
        zf=ZufangItem()
        title_list = response.xpath(".//div[@class='f-list-item ']/dl/dd[1]/a/text()").extract()
        price_list = response.xpath(".//div[@class='f-list-item ']/dl/dd[5]/div[1]/span[1]/text()").extract()
        for i,j in zip(title_list,price_list):
        #     print(i,':',j)
            zf['title'] = i
            zf['price'] = j
            yield zf