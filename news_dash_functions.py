#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import datetime
from datetime import date, timedelta   
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from config import SITE_BLACKLIST, DB_CONNECTION_STRING


def create_news_df(dbConnection):
    news_df = pd.read_sql("select * from news.news_table", dbConnection);
    news_df['Date'] = pd.to_datetime(news_df['Date'])
    news_df = news_df[['Keyword','Title','Date','Link','Site']]
    news_df = news_df[~news_df.Site.isin(SITE_BLACKLIST)]
    news_df = news_df.drop_duplicates(subset=['Title'])
    return news_df



#Create keyword news df
def create_keyword_news(news_df, keyword):
    comp_news_df = news_df[(news_df.Keyword==keyword)]
    last_week = datetime.datetime.now() - timedelta(weeks=1)
    comp_news_df = comp_news_df[(comp_news_df.Date >= last_week)].sort_values('Date', ascending=False).reset_index()
    comp_news_df.drop('index',axis=1)
    comp_news_df['Date'] = comp_news_df['Date'].dt.strftime("%b %d, %Y")
    return comp_news_df

#Create keyword dropdown menu
def get_dropdown_names(dbConnection):
    keywords = pd.read_sql("select distinct Keyword from news.news_table", dbConnection).Keyword.tolist()
    keywords.sort()
    dropdown_list=[]
    for k in keywords:
        dropdown_list.append({'label': k, 'value' : k})
    return dropdown_list
