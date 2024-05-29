#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("C:\Users\Akshara\Downloads\login (2).htm")


# In[3]:


data = pd.read_csv(r"C:\Users\Akshara\Desktop\pyth\covid19_italy_province.csv")


# In[4]:


data = pd.read_csv(r"C:\Users\Akshara\Desktop\pyth\covid19_italy_region.csv")


# In[5]:


data.head()


# In[6]:


data.columns


# In[7]:


data.tail()


# In[8]:


data.describe()


# In[9]:


data.isnull().sum()


# In[11]:


data.columns


# # variable relating with scatterplot
# 

# In[15]:


sns.relplot(x="TotalPositiveCases", y="Recovered", data=data)


# In[16]:


sns.pairplot(data)


# In[18]:


data.columns


# In[19]:


sns.relplot(x='HospitalizedPatients',y ='IntensiveCarePatients',kind ='line',data=data)


# In[20]:


data.columns


# In[21]:


sns.catplot(x = 'IntensiveCarePatients', y ='Deaths',data = data)


# In[22]:


data.columns


# In[25]:


sns.catplot(x = 'Recovered',y ='TotalPositiveCases',data=data)


# In[ ]:




