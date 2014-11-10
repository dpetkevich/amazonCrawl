import scrapy

from amazonCrawl.items import AmazoncrawlItem

class categorySpider(scrapy.Spider):
    name = "categories"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "http://www.amazon.com/Best-Sellers/zgbs/",
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="zg_browseRoot"]/ul/li'):
            item = AmazoncrawlItem()
            item['category'] = sel.xpath('.//a/text()').extract()
            categoryURL=sel.xpath('.//a/@href').extract()
            #print str(categoryURL[0])
            request = scrapy.Request(str(categoryURL[0]), callback=self.categoryParse) 
            request.meta['item'] = item
            yield request

    def categoryParse(self,response):
        item = response.meta['item']
        productURLs=response.xpath('//*[@id="zg_centerListWrapper"]/div/div/div/a/@href')
        print productURLs
        for url in productURLs:

            request = scrapy.Request(url.extract().strip(), callback=self.productParse)
           # print url.extract().strip()
            request.meta['item'] = item
            yield  request
        
    def productParse(self,response):
        item = response.meta['item']

        item['productUrl'] = response.url
        

        if response.xpath('//*[@id="landingImage"]/@src'):
            item['productImage']=response.xpath('//*[@id="landingImage"]/@src').extract()[0]
        #
        if response.xpath('//*[@id="productTitle"]/text()'):
            item['productName']=response.xpath('//*[@id="productTitle"]/text()').extract()[0]
        
        if response.xpath('//*[@id="priceblock_ourprice"]/text()'):
            item['productPrice']=response.xpath('//*[@id="priceblock_ourprice"]/text()').extract()[0]

        if response.xpath("//*[@id='prodDetails']//tr/td[text()='Origin']/following-sibling::td/text()"):
            item['productOrigin']=response.xpath("//*[@id='prodDetails']//tr/td[text()='Origin']/following-sibling::td/text()").extract()[0]

        if response.xpath("//span[starts-with(text(),'Origin:')]/following-sibling::span/text()"):
            item['productOrigin']=response.xpath("//span[starts-with(text(),'Origin:')]/following-sibling::span/text()").extract()[0]

        if response.xpath("//*[starts-with(text(),'Origin:')]/../text()"):
            item['productOrigin']=response.xpath("//*[starts-with(text(),'Origin:')]/../text()").extract()[0]
            
        yield item
        '''
        
        item['productPrice']
        item['productOrigin']
        '''
        #yield item

            
