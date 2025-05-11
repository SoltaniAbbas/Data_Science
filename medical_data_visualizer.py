#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')
df.head()
df.isna().sum()
df.info()
df['overweight']=df.weight/(df.height/100)**2
df.loc[df['overweight']>25,'overweight']=1
df.loc[df['overweight']!=1,'overweight']=0
df.loc[df['cholesterol']==1,'cholesterol']=0
df.loc[df['cholesterol']!=0,'cholesterol']=1
df.loc[df['gluc']==1,'gluc']=0
df.loc[df['gluc']!=0,'gluc']=1

def draw_cat_plot():
    df_cat = df.melt(id_vars = 'cardio', 
                     value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
                     value_name='value')
    df_cat = pd.DataFrame({'Counts':df_cat.groupby(['cardio', 'variable'])['value'].value_counts()})\
                                     .rename(columns={'cardio':'Cardio','variable':'Variable', 'value':'Value'})\
                                     .reset_index()
    catplot = sns.catplot(data=df_cat, x='variable', y='Counts', col='cardio', kind='bar', hue='value')
    fig = catplot.fig
    fig.savefig('CardioPlot.png')
    return fig  
draw_cat_plot()

def draw_heat_map():
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]
    
    corr = df_heat.corr()
    matrix = np.triu(corr)
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, mask=matrix,linewidth=.5,fmt=".1f")
    fig.savefig('Heatmap.png')
    return fig

draw_heat_map()
