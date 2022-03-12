#!/usr/bin/env python
# coding: utf-8

from GoogleNews import GoogleNews
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert
import pymysql
import datetime

from config import DB_CONNECTION_STRING, KEYWORDS


def news_main():
    sqlEngine = create_engine(DB_CONNECTION_STRING, pool_recycle=3600)
    dbConnection = sqlEngine.connect()

    googlenews = GoogleNews()
    googlenews.set_lang('en')
    googlenews.set_period('7d')
    googlenews.set_encode('utf-8')

    news_df = pd.DataFrame()

    for k in KEYWORDS:
        googlenews.get_news(k)
        results = googlenews.results()
        c_news_df = pd.DataFrame(results)
        c_news_df['keyword'] = k
        c_news_df = c_news_df[c_news_df.title.str.contains(k)]
        news_df = news_df.append(c_news_df)

    news_df = news_df[['keyword','title','desc','datetime','link','site']].sort_values(['keyword','datetime'])


    news_df.rename(columns = {'keyword' : 'Keyword', 'title' : 'Title', 'desc' : 'Desc' , 'datetime' : 'Date', 'link' : 'Link', 'site' : 'Site'}, inplace = True)
    news_df['Date'] = pd.to_datetime(news_df['Date'])

    news_df.to_sql("news_table", dbConnection, if_exists='replace', index=False)

    googlenews.clear()



if __name__ == "__main__":
    news_main()

