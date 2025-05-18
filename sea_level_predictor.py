#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')
sns.scatterplot(df,x='Year',y='CSIRO Adjusted Sea Level',label='CSIRO Sea Level')

RegLine = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
y1=RegLine.intercept + RegLine.slope*df.Year
sns.lineplot(df,x=df.Year,y=y1, color='r', label='fitted line')
sns.scatterplot(df,x='Year',y='CSIRO Adjusted Sea Level',label='CSIRO Sea Level')
plt.title('Sea Level by CSIRO')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.show()

dfnew = df[df['Year']>=2000]
RegLine_New = linregress(x=dfnew['Year'], y=dfnew['CSIRO Adjusted Sea Level'])
print(RegLine_New)

x1= dfnew['Year']
y1=dfnew['CSIRO Adjusted Sea Level']
x2=np.arange(2000,2050)
y2=RegLine_New.intercept + RegLine_New.slope*x2
plt.scatter(x1, y1, label='CSIRO Sea Level')
plt.plot(x2, y2, label='fitted line',color='r')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.show()

Pred2050 = RegLine_New.intercept + RegLine_New.slope*2050
print(Pred2050)
