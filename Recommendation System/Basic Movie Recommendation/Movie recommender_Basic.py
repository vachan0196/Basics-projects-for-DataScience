#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


colm_names = ['user_id','item_id','rating','timestamp']


# In[3]:


df = pd.read_csv('u.data',sep = '\t', names = colm_names)


# In[4]:


df.head()


# In[5]:


movie_titles = pd.read_csv('Movie_Id_Titles')


# In[6]:


movie_titles.head()


# In[7]:


df = pd.merge(df,movie_titles, on = 'item_id')


# In[8]:


df.head()


# In[9]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


sns.set_style('white')


# In[11]:


df.groupby('title')['rating'].mean().sort_values(ascending=False).head()


# In[12]:


df.groupby('title')['rating'].count().sort_values(ascending=False).head()


# In[13]:


ratings = pd.DataFrame(df.groupby('title')['rating'].mean())


# In[14]:


ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())


# In[15]:


ratings.head()


# In[16]:


ratings['num of ratings'].hist(bins = 50)


# In[17]:


ratings['rating'].hist(bins=50)


# In[18]:


sns.jointplot(x='rating',y='num of ratings', data = ratings, alpha = 0.4)


# In[19]:


mo_mt = df.pivot_table(index= 'user_id', columns = 'title', values = 'rating')


# In[20]:


mo_mt.head()


# In[21]:


ratings.sort_values('num of ratings',ascending = False).head()


# In[22]:


stw_user_ratings = mo_mt['Star Wars (1977)']
lie_user_ratings = mo_mt['Liar Liar (1997)']


# In[23]:


stw_user_ratings.head()


# In[25]:


same_as_stw = mo_mt.corrwith(stw_user_ratings)


# In[27]:


same_as_lie = mo_mt.corrwith(lie_user_ratings)


# In[32]:


corr_stw = pd.DataFrame(same_as_stw,columns = ['Correlation'])
corr_stw.dropna(inplace = True)
corr_stw = corr_stw.join(ratings['num of ratings'])
corr_stw.head()


# In[33]:


corr_stw[corr_stw['num of ratings']>100].sort_values('Correlation',ascending = False).head()


# In[35]:


corr_lie = pd.DataFrame(same_as_lie,columns = ['Correlation'])
corr_lie.dropna(inplace = True)
corr_lie = corr_lie.join(ratings['num of ratings'])
corr_lie.head()


# In[37]:


corr_lie[corr_lie['num of ratings']>100].sort_values('Correlation', ascending = False).head()


# In[ ]:




