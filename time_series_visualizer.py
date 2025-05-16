#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pd.options.mode.copy_on_write = True

df = pd.read_csv("fcc-forum-pageviews.csv")
df.head()
df.isna().sum()
df.date=pd.to_datetime(df.date)
df = df.set_index('date')
df_clr=df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
df_clr

def draw_line_plot():
    fig=plt.subplots(figsize=(32, 10))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize = 30)
    plt.xlabel("Date", fontsize = 25)
    plt.ylabel("Page Views", fontsize = 25)
    fig=plt.plot(df_clr, color='green')
    plt.savefig('Line_Plot.jpg')
    return fig
    
draw_line_plot()
df_clr['year']=df_clr.index.year
df_clr['month']=df_clr.index.month
df_clr['namemonth']=df_clr.index.month_name()
df_clr

def draw_bar_plot():
    df_bar = df_clr.copy()
    fig=plt.subplots(figsize=(32, 20))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize = 30)
    plt.xlabel("Date", fontsize = 25)
    plt.ylabel("Page Views", fontsize = 25)
    df_bar.groupby(['year','namemonth'], sort=False).value.mean().round().astype(int)
    sns.barplot(df_bar, x="year",y='value', hue="namemonth", palette="tab10", width=0.5, gap=.1,errorbar=('ci', 0))
    plt.legend(fontsize='30', title_fontsize='14')
    plt.savefig('Bar_Plot.jpg')
    return fig
   
draw_bar_plot()

def draw_box_plot():
    df_box =df_clr.copy()
    plt.figure(figsize=(32, 10))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(df_box, x="year", y="value")
    plt.title("Year-wise Box Plot (Trend)", fontsize = 30)
    plt.xlabel("Year", fontsize = 25)
    plt.ylabel("Page Views", fontsize = 25)
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    
    
    plt.subplot(1, 2, 2)
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box['monthname'] = [d.strftime('%b') for d in df_box.index]
    sns.boxplot(df_box, x='monthname', y="value", order=month_order,hue='monthname')
    plt.title("Month-wise Box Plot (Seasonality)", fontsize = 30)
    plt.xlabel("Month", fontsize = 25)
    plt.ylabel("Page Views", fontsize = 25)
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    
    plt.savefig('Box_Plot.png')
    return 

draw_box_plot()