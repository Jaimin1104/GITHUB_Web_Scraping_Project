# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubtopicsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topics_name = scrapy.Field()
    topics_url = scrapy.Field()
    topics_description = scrapy.Field()
