#!/usr/bin/env python
# coding: utf-8
import pandas as pd
names=['age', 'workclass', 'fnlwgt', 'education', 'education-num',
       'marital-status', 'occupation', 'relationship', 'race', 'sex',
       'capital-Gain', 'capital-Loss', 'hoursPerWeek', 'nativeCountry',
       'salary']
df = pd.read_csv( 'adult.data',header=None,names=names )
df.head()
df.info()
df.isnull().sum()

# ###### How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)

df.race.value_counts()

# ##### What is the average age of men?

Men_mean_age=df[df.loc[:,'sex']=='Male'].age.mean()
print(f'Men mean age is  = {Men_mean_age:.1f}')

####### What is the percentage of people who have a Bachelor's degree?

Qty_Bachelor=len(df[df.loc[:,'education']=="Bachelors"])
Qty_total_education=len(df.education)

Bachelor_percent=round(Qty_Bachelor/Qty_total_education*100,2)
print(Bachelor_percent)

# ##### What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
df_advance_edu=df.query('(salary==">50K") and (education in["Bachelors","Masters","Doctorate"])' )
percent_h50K_edu=len(df_advance_edu)/len(df)*100
print(round(percent_h50K_edu,1))

# #### What percentage of people without advanced education make more than 50K?

df_notadvance_edu=df.query('(salary==">50K") and (education not in["Bachelors","Masters","Doctorate"])' )
percent_h50K_wa_edu=len(df_notadvance_edu)/len(df)*100
print(round(percent_h50K_wa_edu,1))

# ##### What is the minimum number of hours a person works per week?

df.hoursPerWeek.min()

# ##### What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

df_hpw1=df.query('(salary==">50K") and (hoursPerWeek ==1)' )

percent_hpw1=len(df_hpw1)/len(df)*100
print(round(percent_hpw1,2))

# ###### What country has the highest percentage of people that earn >50K and what is that percentage?

df_country=df.query('salary ==">50K" and nativeCountry')
df_country.to_csv('contry.csv')
def most_frequent(lst):
    return max(set(lst), key=lst.count)

result = most_frequent(list(df_country.nativeCountry))
print(f"Most frequent element: {result}")
mask=df_country.loc[: , 'nativeCountry']=='United-States'
round(len(df_country[mask])/len(df)*100,1)


# ##### Identify the most popular occupation for those who earn >50K in India.
df_most_job_india=df.query('salary ==">50K" and nativeCountry == "India" and occupation ')
df_most_job_india.occupation.value_counts()
most_frequent(list(df_most_job_india.occupation))


 




