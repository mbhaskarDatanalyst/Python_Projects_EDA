#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
#For visualizaton
import matplotlib.pyplot as plt
#For regular expression
import re
#For handling strings
import string
#FOr performing mathematical operations
import math


# In[2]:


#import dataset
df=pd.read_csv(r"C:\Users\Mithu Bhaskar\Downloads\news_syn.csv")


# In[3]:


df.head()


# In[4]:


print('Shape of data=>,df.shape')


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df


# In[8]:


df.info()


# In[9]:


#Drop null values
df.dropna(inplace=True)


# In[10]:


df.info()


# In[11]:


df.isnull().sum()


# In[12]:


df.head(10)


# In[13]:


df['Article category'].unique()


# In[14]:


#How many different values are there
df['Article category'].value_counts()


# In[15]:


#Replcae and collapse of data
mappings={'STYLE':'STYLE & BEAUTY',
    'ARTS':'ARTS & CULTURE',
    'CULTURE & ARTS':'ARTS & CULTURE',
    'BLACK VOICES':'VOICES',
    'LATINO VOICES':'VOICES',
    'HEALTHY LIVING':'LIVING',
    'HOME & LIVING':'LIVING'}


# In[16]:


df['Article category']= df['Article category'].replace(mappings)


# In[17]:


df['Article category'].unique()


# In[18]:


df['Article category'].value_counts()


# In[19]:


df.head()


# In[20]:


#Drop news link--scrap data
df.drop(['news_link'], axis=1, inplace= True)


# In[21]:


df.head()


# In[22]:


df['Author'].unique()


# In[23]:


mappings={'Shawn Amos, Contributor\nblues preacher | content junkie | doughnut lover':'Shawn Amos',
         'Matt Wilstein, Contributor\nEditor, Gotcha Media Blog':'Matt Wilstein',
         'Mary Kincaid, Contributor\nFounder and Editor of Zuburbia.com':'Mary Kincaid',
         'Arianna Huffington, Contributor':'Arianna Huffington',
         'Refinery29, ContributorThe #1 new-media brand for smart, creative and stylish women e...':'Refinery29',
         'Robert Siciliano CSP, Contributor\nPersonal Security, Privacy, Cyber Safety and Identity Theft Ex...':'Robert Siciliano',
         'The Atlantic, ContributorExploring the American idea since 1857':'The Atlantic'}


# In[24]:


df['Author']=df['Author'].replace(mappings)


# In[25]:


df['Author'].unique()


# In[44]:


df.head(10)


# In[27]:


df['News Headline'].unique()


# In[28]:


df['News Headline'].value_counts()


# In[29]:


df['short_description'].unique()


# In[30]:


df['short_description'].value_counts()


# In[31]:


df.info()


# In[48]:


df.head(10)


# In[33]:


#Considering those Article having news headlines atleast 50
df=df.groupby('Article category').filter(lambda x:len(x)>50).reset_index(drop=True)
print()


# In[34]:


df.info()


# In[36]:


#Convert datetime  to date
df['date'] = pd.to_datetime(df['date'])


# In[39]:


df['year'] = df['date'].dt.year


# In[40]:


df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day


# In[41]:


df.head()


# In[42]:


df.info()


# In[55]:


import seaborn as sns
df.groupby('Article category')['Article category'].count().plot.pie(autopct='%.2f',figsize=(10,10))


# In[54]:


df['Article category'].unique()


# In[71]:


sns.set(rc={'figure.figsize':(20,5)})

ax = sns.countplot(data=df, y='Article category')
for bars in ax.containers:
    ax.bar_label(bars)


# In[72]:


sns.set(rc={'figure.figsize':(40,20)})

ax = sns.countplot(data=df, y='News Headline')
for bars in ax.containers:
    ax.bar_label(bars)


# In[73]:


#top 5 Articles on the basis of news headlines
top_five_articles=df.groupby('Article category').count().sort_values(by='News Headline', ascending=False)['News Headline'][:5]
top_five_articles


# In[75]:


sns.set(rc={'figure.figsize':(10,5)})
top_five_articles.plot.barh()
plt.show()


# In[77]:


#Finding top 5 authors 
top_five_Authors=df.groupby('Author').count().sort_values(by='News Headline', ascending=False)['News Headline'][:5]
top_five_Authors


# In[79]:


sns.set(rc={'figure.figsize':(10,5)})
top_five_Authors.plot.barh()
plt.show()


# In[91]:


#Top 5 headlines which are printed in the news frequently
top_five_Headlines=df.groupby('News Headline').count().sort_values(by='short_description', ascending=True)['short_description'][:5]
top_five_Headlines


# In[92]:


sns.set(rc={'figure.figsize':(10,5)})
top_five_Headlines.plot.barh()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




