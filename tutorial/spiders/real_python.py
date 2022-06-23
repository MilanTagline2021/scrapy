import scrapy
from tutorial.items import RealPythonbotItem, AmazonItem

class RealPythonSpider(scrapy.Spider):
    name = "realpython"
    start_urls = [
        # "https://quotes.toscrape.com/"
        "https://www.amazon.in/s?i=stripbooks&bbn=976390031&rh=n%3A976389031%2Cn%3A4149493031%2Cp_n_publication_date%3A2684819031&dc&qid=1654075738&rnid=976390031&ref=sr_nr_n_16"
    ]

    def parse(self, response):
        print("*"*100)
        book_name = response.css(".a-size-medium::text").extract()
        book_image = response.css(".s-image::attr(src)").extract()
        book_author = response.css(".a-color-secondary .a-size-base.s-link-style::text").extract()
        book_price = response.css(".s-price-instructions-style .a-price-whole::text").extract()

        print(book_name)
        print("*"*100)
        print(book_image)
        print("*"*100)
        print(book_author)
        print("*"*100)
        print(book_price)
        print("*"*100)


    # def parse(self, response):
    #     for new_url in response.xpath('//div[@class="a-section a-spacing-none shogun-widget deals-shoveler fresh-shoveler"]'):
    #         data_dict = AmazonItem()
    #         data_dict['h2'] = new_url.xpath('.//div[@class="a-cardui-header as-title-block"]//h2[@class="a-color-base as-title-block-left"]/text()').extract()
    #         data_dict['anchor'] = new_url.xpath('.//div[@class="a-cardui-header as-title-block"]//a/@href').extract()
    #         data_dict['div'] = response.xpath('.//div[@class="a-section a-spacing-none feed-carousel first-carousel"]//div[@class="a-section feed-carousel-viewport"]/ul/li/text()').extract()
    #         print(data_dict['div'])
    #     # for kept in 
    #     #     k = kept.xpath('.//div[@class="a-section feed-carousel-viewport"]/ul/li/text()').extract()
    #     #     print(k, "£"*100)
    
    #     for quote in response.xpath('//div[@class="quote"]'):
    #         item = RealPythonbotItem()
    #         item['text'] = quote.xpath('.//span[@class="text"]/text()').extract()
    #         item['author'] = quote.xpath('.//small[@class="author"]/text()').extract()
    #         item['tags'] = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()

    #         print(item, "*"*100)
   
