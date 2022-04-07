# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 20:18:27 2022

@author: Sagar
"""
from textblob import TextBlob
import pandas as pd
import numpy as np
import yfinance as yf

def training(news):
    df = pd.DataFrame(news, columns=['news'])
    df['polarity'] = np.nan
    df['subjectivity'] = np.nan
    df['score'] = np.nan

    for i, n in enumerate(df['news']):
        sent_analysis = TextBlob(n)
        df['polarity'].iloc[i] = sent_analysis.sentiment.polarity
        df['subjectivity'].iloc[i] = sent_analysis.sentiment.subjectivity
        
        if sent_analysis.sentiment.polarity >= 0.05:
            score1 = 'positive'
        elif -0.05 < sent_analysis.sentiment.polarity < 0.05:
            score1 = 'neutral'
        else:
            score1 = 'negative'
        df['score'].iloc[i] = score1   
        
    return df

news_data = [ ]
msft = yf.Ticker("MSFT")


l = len(msft.news)
for i in range(l):
    news_data.append(msft.news[i]['title'])
stk_sentiment = training(news_data)
del stk_sentiment['news']
print(stk_sentiment)

