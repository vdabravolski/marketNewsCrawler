from textblob import TextBlob

text = "Raymond James analyst Christopher Caso says Apple (NASDAQ:AAPL) " \
       "hasn't started final production on the iPhone X due to a late delay, " \
       "which could push back device supplies to December. "


def get_sentiment(text):
    blob = TextBlob(text)

    polarity = []
    subjectivity = []

    for sentence in blob.sentences:
        polarity.append(sentence.sentiment.polarity)
        subjectivity.append(sentence.sentiment.subjectivity)

    avg_polarity, avg_subjectivity = 0, 0
    if len(polarity) != 0 and len(subjectivity) != 0:
        avg_polarity = sum(polarity) / len(polarity)
        avg_subjectivity = sum(subjectivity) / len(subjectivity)

    return avg_polarity, avg_subjectivity


if __name__ == '__main__':
    get_sentiment(text=text)
