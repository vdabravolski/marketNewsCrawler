# -*- coding: utf-8 -*-

# Scrapy settings for seeking_alpha project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'seeking_alpha'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['seeking_alpha.spiders']
NEWSPIDER_MODULE = 'seeking_alpha.spiders'

RETRY_ENABLED = True
RETRY_TIMES = 10  # initial response + 2 retries = 3 requests
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]
RETRY_PRIORITY_ADJUST = -1

CONCURRENT_REQUESTS = 1
DOWNLOADER_STATS = False
DOWNLOAD_DELAY = 5


# # Crawl responsibly by identifying yourself (and your website) on the user-agent

DOWNLOADER_MIDDLEWARES = {
    'seeking_alpha.middlewares.RotateUserAgentMiddleware': 110,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 150,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 200
}

USER_AGENT_CHOICES = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"
]

EXTENSIONS = {
    'scrapy.extensions.closespider.CloseSpider': 500
}

ITEM_PIPELINES = {
    'seeking_alpha.pipelines.NewsToPandas': 300,
#    'seeking_alpha.pipelines.NewsToCorpus': 400,
#    'seeking_alpha.pipelines.JsonWriterPipeline': 310,
}

