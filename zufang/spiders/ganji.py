import scrapy
from ..items import ZufangItem #..items的前一个点是本文件夹中所有，同一个包

'''
新建的spider文件，是一个类
'''
class GanjiSpider(scrapy.Spider): #必须继承scrapy.Spider类
    name = 'zufang' #定义name属性，需要包含爬虫名
    start_urls = ['http://bj.ganji.com/fang1/'] #需要包含用于下载的初始URL，自动调用start_requests()

    def parse(self, response): #parse是spider的一个方法
        '''
        被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
        该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象

        Scrapy为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，并将 parse 方法作为回调函数(callback)赋值给了Request
        Request对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法
        '''
        print(response)
        '''
        输入 response.body 将输出response的包体， 输出 response.headers 可以看到response的包头
        '''

        '''
        scrapy用XPATH和css选择器选择元素，也可以用BS/LXML（ 基于ElementTree (不是Python标准库的一部分)的python化的XML解析库）
        response.selector.xpath(),返回该表达式所对应的所有节点的selector list列表
        response.css(),返回该表达式所对应的所有节点的selector list列表
        下面俩跟在上面俩后
        .extract（），序列化该节点为unicode字符串并返回list
        .re(): 根据传入的正则表达式对数据进行提取，返回unicode字符串list列表
        '''
        title_list = response.xpath(".//div[@class='f-list-item ']/dl/dd[1]/a/text()").extract()
        price_list = response.xpath(".//div[@class='f-list-item ']/dl/dd[5]/div[1]/span[1]/text()").extract()

        '''
        XPATH可以进行拼接进一步获取节点如下,嵌套选择器：
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            print title, link, desc
        '''
        zf = ZufangItem()
        '''Item 对象是自定义的python字典dictionary-like),KEY即在items.py中用Field赋值的属性，使用item可以给数据更好的结构性，不用也可以'''

        for i,j in zip(title_list,price_list):
            '''
            这里为item的key赋值，值为选择器选择后的结果
            '''
            zf['title'] = i
            zf['price'] = j

            yield zf #返回item对象，由于类dict，可以用ins.items()

            #item2=item.copy()