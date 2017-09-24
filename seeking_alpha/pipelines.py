# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pickle
import pandas as pd
import helpers
from datetime import date, timedelta
import json


class NewsToPandas(object):  # Pipeline to clean news from HTML
    def open_spider(self, spider):
        self.spider = spider
        self.ticker = spider.ticker
        self.filepath = "/Users/vadzimdabravolski/seeking_alpha/output/"+self.ticker + '_news_df.p'
        self.news_df = pd.DataFrame(columns=['content', 'polarity', 'subjectivity', 'datetime', 'ticker'])

    def process_item(self, item, spider):
        # Cleaning of the content
        content = item['content']
        content = ''.join(content)  # get string from list of strings
        dec_content = content.encode('ascii', 'ignore').decode('ascii')
        content = " ".join(dec_content.split()) #remove extensive white spaces.
        polarity, subjectivity = helpers.get_sentiment(content)
        datetime = pd.to_datetime(
            self._convert_datetime(item['datetime'][0]))
        ticker = item['ticker']

        dict = {'ticker':ticker, 'datetime':datetime, 'content': content, 'polarity':polarity, 'subjectivity':subjectivity}
        self.news_df = pd.concat([self.news_df, pd.DataFrame(dict, index=[0])])
        return item


    def _convert_datetime(self, dt_string):
        '''
        There are two formats of date time data on Seeking Alpha:
            - Oct. 27, 2015, 4:58 PM - for news from previous years
            - Thu, Sep. 7, 12:44 PM - for this year news
        So this methid tries to convert datetime data point to one of the formats and returns the succesful one as pandas Timestamp.
        '''

        try:
            dt = pd.to_datetime(dt_string, format='%a, %b. %d, %Y, %H:%M %p')
        except ValueError:
            try:
                dt = pd.to_datetime(dt_string, format='%b. %d, %Y, %H:%M %p')
            except ValueError:
                try:
                    dt = pd.to_datetime(dt_string, format='%a, %b. %d, %H:%M %p')
                    dt = dt.replace(year=2017)
                except ValueError:
                    try:
                        dt = pd.to_datetime(dt_string, format='%a, %b %d, %H:%M %p')
                        dt = dt.replace(year=2017)
                    except ValueError:
                        try:
                            dt = pd.to_datetime(dt_string, format='%b %d, %Y, %H:%M %p')
                        except:
                            if ('today' in dt_string.lower()):
                                dt =pd.to_datetime(date.today())
                            elif ('yesterday' in dt_string.lower()):
                                dt = pd.to_datetime(date.today()-timedelta(1))
                            else:
                                print(dt_string)  # need to differentiate between today and yesterday
                                dt = date.today()

        return dt

    def close_spider(self, spider):
        self.news_df = self.news_df.reset_index(drop=True)
        self.news_df.to_pickle(self.filepath)


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
