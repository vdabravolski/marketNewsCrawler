import subprocess
import pickle
import pandas as pd



if __name__ == '__main__':
    # retrieve all SP500 files from prepared dataframe
    with open('sp500.p','rb') as file:
        ticker_df = pickle.load(file)

    tickers = ticker_df.ticker.tolist()

    for _, ticker in enumerate(tickers):
        scrapy_command = 'scrapy runspider seeking_alpha/spiders/seekingAlpha.py -a ticker={0}'.format(ticker)
        # https://stackoverflow.com/questions/42203525/running-scrapy-crawler-from-a-main-function
        process = subprocess.check_call(scrapy_command, shell=True)
