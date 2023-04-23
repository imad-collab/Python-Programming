#!/usr/bin/env python
# coding: utf-8

# ## Modules

# In[ ]:


#Ex:1

import math


# In[ ]:


x = 16
math.sqrt(x)


# In[ ]:


math.pow(2,5)


# In[ ]:


dir(math)


# In[ ]:


#Ex:2

import calendar


# In[ ]:


cal = calendar.month(2021,8)


# In[ ]:


print(cal)


# In[ ]:


calendar.isleap(2018)


# In[ ]:


calendar.isleap(2021)


# In[ ]:


dir(calendar)


# In[ ]:


#Ex.3
import datetime


# In[ ]:


x = datetime.datetime.now()
print(x)


# In[ ]:


y=datetime.date.today()
print(y)


# In[ ]:


dir(datetime)


# In[ ]:


a=datetime.date(1985,1,20)
print(a)


# In[ ]:


a.year


# In[ ]:


a.month


# In[ ]:


a.day


# In[ ]:


x_date=datetime.date(2020,1,20)


# In[ ]:


x_time=datetime.time(20,25,0)


# In[ ]:


x_datetime=datetime.datetime(2021,1,20,20,25,0,0)


# In[ ]:


print(x_date)


# In[ ]:


print(x_time)


# In[ ]:


print(x_datetime)


# ## Dataframe

# In[ ]:


import pandas as pd
import numpy as np
from pandas import DataFrame,Series


# In[ ]:


import webbrowser


# In[ ]:


website = 'https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html'


# In[ ]:


webbrowser.open(website)


# In[ ]:


df= pd.read_clipboard()


# In[ ]:


df


# ## Creating dataframes using numpy and dictionaries

# In[ ]:


x=np.array([[1,2,3],[4,5,6]])
x


# In[ ]:


dict1=DataFrame({'col1':[1,2,3],"col2":[4,5,6]})
dict1


# In[ ]:


## Read a csv file
df1 = pd.read_csv('Universities.csv')


# In[ ]:


df1


# In[ ]:


type(df1)


# In[ ]:


df1 = pd.read_csv('Universities.csv',nrows = 2)
df1


# In[ ]:


df1 = pd.read_csv('Universities.csv',usecols=[1,3])
df1


# In[ ]:


df1.columns


# In[ ]:


df1[['SAT','Accept']]


# In[ ]:


df1.head()


# In[ ]:


df1.head(10)


# In[ ]:


df1.tail()


# In[ ]:


df1.tail(10)


# In[ ]:


df1.head()


# In[ ]:


df1.iloc[2]


# In[ ]:


df1.iloc[3:6]


# In[ ]:


df2 = pd.read_csv('Universities.csv')
df2.head()


# In[ ]:


df2 = pd.read_csv('Universities.csv',index_col = 'Univ')
df2


# In[ ]:


df2.loc['Yale']


# In[ ]:


df2.iloc[2]


# In[ ]:


df2.loc[['UVA','Yale']]


# In[ ]:


df2.loc['UVA':'Yale']


# In[ ]:


df2.shape


# In[ ]:


x= df2.drop('Yale')
x


# In[ ]:


x.shape


# In[ ]:


y = df2.drop('Top10', axis =1)
y


# In[ ]:


y.shape


# In[ ]:


df2.head()


# In[ ]:


df2.describe()


# ## Handling with null values

# In[ ]:


dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])


# In[ ]:


dframe


# In[ ]:


new_frame= dframe.dropna() # Drop the rows having na 
new_frame


# In[ ]:


new_frame=dframe.dropna(how='all')  # Drop the rows having na's in all the rows
new_frame


# In[ ]:


new_frame=dframe.dropna(axis = 1)  # Drop the Columns having na's in all the columns
new_frame


# In[ ]:


dframe


# In[ ]:


dframe.dropna(thresh = 2) # Drop the rows not having  atleast 2 values


# In[ ]:


dframe.fillna(1)

