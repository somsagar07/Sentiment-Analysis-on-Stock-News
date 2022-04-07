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
hist = msft.balance_sheet
print(hist)
news_data = [
        "Tesla Inc. gained another 2,8% on Wednesday and is now up 1,560% in the past 18 months Tesla bulls are betting the stock’s insane run will continue following a Democratic Senate sweep in Georgia, some Tesla option traders are dumping massive amounts of call options on Wednesday",
        "Most of the analysis on this stock right now has to do with the Pfizer Inc. highly-touted COVIS-19 vaccine which is now making waves through global markets. That said, even before the vaccine was released, I saw tremendous value in this stock, and the same is true of the stock’s current valuation relative to its peers and its growth potential",      
        "IPhone suppliers are racing to meet surging demand for Apple Inc.’s 5G handsets after tech-savvy consumers leaped on the first major wireless technology upgrade in a decade. The number suggest the world may finally be warming to 5G with its much faster download speeds and more reliable connections. However, Europe's less profitable phone industry has avoided a headlong plung into 5G, wary of rolling out expensive services that consumers won't be ready to pay for."
    ]
stk_sentiment = training(news_data)
del stk_sentiment['news']
print(stk_sentiment)

