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

DOWNLOADER_STATS = False
DOWNLOAD_DELAY = 3


# # Crawl responsibly by identifying yourself (and your website) on the user-agent

DOWNLOADER_MIDDLEWARES = {
    'seeking_alpha.middlewares.RotateUserAgentMiddleware': 110,
}

USER_AGENT_CHOICES = [
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
]

EXTENSIONS = {
    'scrapy.extensions.closespider.CloseSpider': 500
}

ITEM_PIPELINES = {
    'seeking_alpha.pipelines.NewsToPandas': 300,
#    'seeking_alpha.pipelines.NewsToCorpus': 400,
#    'seeking_alpha.pipelines.JsonWriterPipeline': 310,
}

