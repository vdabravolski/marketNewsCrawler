#!/usr/local/bin/python
# coding: utf-8

from textblob import TextBlob

text = "Raymond James analyst Christopher Caso says Apple (NASDAQ:AAPL) " \
       "hasn't started final production on the iPhone X due to a late delay, " \
       "which could push back device supplies to December. "

def get_sentiment(text):


    blob = TextBlob(text)
    blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                        #  ('threat', 'NN'), ('of', 'IN'), ...]

    print(blob.noun_phrases)

    for sentence in blob.sentences:
        print(sentence)
        print(sentence.sentiment.polarity)

if __name__ == '__main__':
    get_sentiment(text=text)
