#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[11]:


weather = pd.read_csv(r"C:\Users\User\Desktop\weather.csv")


# In[13]:


weather


# In[14]:


weather.head()


# In[16]:


#find all the unique 'Wind Speed' values in the data


# In[17]:


weather.head(2)


# In[18]:


weather.nunique()


# In[21]:


weather['Wind Speed_km/h'].unique()


# In[23]:


weather.Weather.value_counts()


# In[26]:


weather[weather.Weather == "Clear"]


# In[27]:


# find the number of times when the "wind speed was exactly 3km/h"


# In[29]:


weather[weather['Wind Speed_km/h']== 4]


# In[30]:


# find the null values in the data


# In[31]:


weather.isnull().sum()


# In[32]:


#Rename the column name 'Weather' of the dataframe to 'Weather condition'


# In[42]:


weather.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)


# In[43]:


weather.head()


# In[44]:


# what is the mean Visibility


# In[45]:


weather.Visibility_km	.mean()


# In[46]:


#what is the standard deivation of 'pressure' in this data


# In[47]:


weather.Press_kPa.std()


# In[48]:


# what is the variance of 'Relative Humidity' in this data


# In[54]:


weather["Rel Hum_%"].var()


# In[55]:


#find all intances when 'Snow' was recorded


# In[56]:


weather[weather['Weather Condition'] == 'Snow']


# In[57]:


# find all the instances when 'Wind speed is above 24' and visibility is 25'


# In[64]:


weather[(weather['Wind Speed_km/h']> 24) & (weather['Visibility_km'] == 25)]


# In[ ]:





# In[ ]:




