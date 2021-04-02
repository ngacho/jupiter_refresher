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
said_no = df[df['Hobbyist'] == 'No']
#find those who said yes to being a hobbyist
said_yes = df[df['Hobbyist'] == 'Yes']
##print the mean of those ages
print("Average age of non-hobbyists is " + str(said_no['Age'].mean()))
print("Average age of hobbyists is " + str(said_yes['Age'].mean()))






