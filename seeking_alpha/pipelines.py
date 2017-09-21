# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize


class NewsCleaning(object):  # Pipeline to clean news from HTML
    def open_spider(self, spider):
        self.ticker = spider.ticker
        new_file = "/Users/vadzimdabravolski/seeking_alpha/output/"+self.ticker + '_ticker_news.jl'
        self.file = open(new_file, 'w')
        spider.log("File created:".format(new_file))

    def process_item(self, item, spider):
        # Cleaning of the content
        content = item['content']
        content = ''.join(content)  # get string from list of strings
        dec_content = content.encode('ascii', 'ignore').decode('ascii')
        item['content'] = " ".join(dec_content.split()) #remove extensive white spaces.

        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()




class NewsToCorpus(object):

    def open_spider(self, spider):
        self.ticker = spider.ticker
        corpus_file = "/Users/vadzimdabravolski/seeking_alpha/output/News_corpus.jl"
        self.file = open(corpus_file, "a+")

    def process_item(self, item, spider):
        # Adding news content to the corpus file
        self.file.write(item['content']+"\n")
        return item

    def close_spider(self, spider):
        self.file.close()
