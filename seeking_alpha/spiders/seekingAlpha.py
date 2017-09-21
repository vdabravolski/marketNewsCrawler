# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
import seeking_alpha.items
import seeking_alpha.middlewares
import json
from scrapy.selector import Selector
from scrapy.exceptions import CloseSpider

class SeekingalphaSpider(scrapy.Spider):
    name = "seekingAlpha"
    # download_delay = 1
    allowed_domains = ["seekingalpha.com"]
    start_urls = (
        'http://www.seekingalpha.com/',
    )

    rotate_user_agent = True

    def __init__(self, ticker, max_pages=100):
        super(SeekingalphaSpider)
        self.ticker = ticker
        self.page_count = 0
        self.max_pages = max_pages

    def start_requests(self):
        self.ticker = getattr(self, 'ticker', 'aapl')
        self.base_url = 'https://seekingalpha.com/symbol/'
        ticker_url = '{0}/news/more_news_all?page={1}'.format(self.ticker, self.page_count)
        yield scrapy.Request(self.base_url+ticker_url, self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        html = data['html']
        news_feed = Selector(text=html).xpath('//div[@class="mc_list_texting right bullets"]').extract()

        if len(news_feed) == 0:
            raise CloseSpider('No more news avialable')

        self.log("Parsing page {0}. Number of news found {1}".format(response.url,len(news_feed)), level=log.INFO)
        for news in news_feed:
            item = seeking_alpha.items.NewsItem()
            item['ticker'] = self.ticker
            item['content'] = Selector(text=news).xpath('//span[@class="general_summary light_text bullets"]/ul/li/text()').extract()
            item['url'] = response.url
            item['datetime'] = Selector(text=news).xpath('//span[@class="date pad_on_summaries"]/text()').extract()
            yield item


        if self.page_count < self.max_pages:
            self.page_count += 1
            yield scrapy.Request(self.base_url+'{0}/news/more_news_all?page={1}'.format(self.ticker, self.page_count))
        else:
            raise CloseSpider('Max number of pages to scrape is reached') #stop crawling if we hit the max number of pages.
