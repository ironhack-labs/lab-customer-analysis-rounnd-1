#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd


# In[58]:


df1 = pd.read_csv('files_for_lab/csv_files/file1.csv', sep=',')
df1


# In[59]:


df1.shape


# In[60]:


df2 = pd.read_csv('files_for_lab/csv_files/file2.csv', sep=',')
df2


# In[61]:


df2.shape


# In[62]:


df3 = pd.read_csv('files_for_lab/csv_files/file3.csv', sep=',')
df3


# In[63]:


df3.shape


# In[64]:


df1.rename(columns={'ST':'STATE'})


# In[65]:


df2.columns


# In[66]:


df2.rename(columns={'ST':'STATE'})


# In[67]:


df3.rename(columns={'Gender':'GENDER'})


# In[68]:


df1.columns = df1.columns.str.upper().str.replace(" ", "_")
df1


# In[69]:


df1.rename(columns={'ST':'STATE'})


# In[70]:


df2.columns = df2.columns.str.upper().str.replace(" ", "_")
df2


# In[71]:


df2.rename(columns={'ST':'STATE'})


# In[72]:


df3.columns = df3.columns.str.upper().str.replace(" ", "_")
df3


# In[73]:


df3.rename(columns={'ST':'STATE'})


# In[74]:


data = pd.concat([df1,df2, df3], axis=0)
data


# In[75]:


data.shape


# In[76]:


data.rename(columns={'ST':'STATE'})


# In[77]:


data.drop_duplicates()


# In[78]:


print(len(data.columns))


# In[79]:


print(data.size)


# In[80]:


data = data.drop(columns=["EDUCATION", "NUMBER_OF_OPEN_COMPLAINTS"])
data


# In[81]:


type(data)


# In[84]:


data.dtypes


# In[85]:


data = data.reset_index(drop=True)
for i in range(len(data['CUSTOMER_LIFETIME_VALUE'])):
    if isinstance(data['CUSTOMER_LIFETIME_VALUE'][i], str) and '%' in data['CUSTOMER_LIFETIME_VALUE'][i]:
        data['CUSTOMER_LIFETIME_VALUE'][i] = float(data['CUSTOMER_LIFETIME_VALUE'][i].replace('%', '')) * 100

data['CUSTOMER_LIFETIME_VALUE'] = pd.to_numeric(data['CUSTOMER_LIFETIME_VALUE'])

display(data)


# In[88]:


data = data.copy()


# In[92]:


display(data.copy)


# In[ ]:




