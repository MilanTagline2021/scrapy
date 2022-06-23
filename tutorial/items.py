# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class RealPythonbotItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class AmazonItem(scrapy.Item):
    h2 = scrapy.Field()
    anchor = scrapy.Field()
    div = scrapy.Field()