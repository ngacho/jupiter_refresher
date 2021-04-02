#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
from pathlib import Path



#display charts inline
#get_ipython().run_line_magic('matplotlib', 'inline')

#path to file
file_to_open = "D:\\Project\\python_playground\\csv\\developer_survey_2020\\survey_results_public.csv"

df = pd.read_csv(file_to_open)

#find the number of answers and columns in our data set
print(df.shape)

#choose the hobbist from the data frame
raw_values = df['Hobbyist'].value_counts()
print(raw_values)

#represent the value counts as a percentage
percentages = df['Hobbyist'].value_counts(normalize=True)
print(percentages)

#plot hobbyist results into a bar
#df['Hobbyist'].value_counts().plot(kind="bar")


#plotting how important education is to one's career.
#df['NEWEdImpt'].value_counts(normalize=True).plot(kind="bar")


#find those who said no to being a hobbyist
non_hobbyists = df[df['Hobbyist'] == 'No']
#find those who said yes to being a hobbyist
hobbyists = df[df['Hobbyist'] == 'Yes']
##print the mean of those ages
print("Average age of non-hobbyists in the world as per the survey is " + str(non_hobbyists['Age'].mean()))
print("Average age of hobbyists in the world as per the survey is " + str(hobbyists['Age'].mean()))

#find hobbyists from a specific country
#filtered_by_country = hobbyists[df['Country'] == 'United States']
filtered_by_country = df[(df['Hobbyist'] == 'Yes') & (df['Country'] == 'United States')]
print("Average age of hobbyists in the US is " + str(filtered_by_country['Age'].mean()))

#analyze the languages preferred by hobbyists
lang_lists = hobbyists['LanguageWorkedWith'].str.split(';', expand=True)
lang_lists.stack().value_counts().plot(kind='bar', figsize=(15, 7), color="#61d199")
