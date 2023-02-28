import scrapy
from ..items import GithubtopicsItem

class TopicspiderSpider(scrapy.Spider):
    name = 'TopicSpider'
    allowed_domains = ['www.github.com']
    page_number = 1
    start_urls = ['http://www.github.com/']

    def parse(self, response):
        while TopicspiderSpider.page_number < 7:
            next_url = TopicspiderSpider.start_urls[0] + 'topics?page=' + str(TopicspiderSpider.page_number)
            yield scrapy.Request(next_url, callback=self.parse_topics)
            TopicspiderSpider.page_number = TopicspiderSpider.page_number + 1
            
    def parse_topics(self, response):
        items = GithubtopicsItem()
        topics_name = response.css('.flex-1 .Link--primary::text').extract()
        topics_url = response.css('.flex-1::attr(href)').extract()
        topics_descriptions = response.css('.flex-1 .color-fg-muted::text').extract()
        for i in range(len(topics_url)):
            topics_url[i] = TopicspiderSpider.start_urls[0] + topics_url[i]
            topics_descriptions[i] = topics_descriptions[i].strip()    
        for i in range(len(topics_name)):
            items['topics_name'] = topics_name[i]
            items['topics_url'] = topics_url[i]
            items['topics_description'] = topics_descriptions[i]
            yield items