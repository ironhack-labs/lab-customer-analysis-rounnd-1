#!/usr/bin/env python
# coding: utf-8

# In[999]:


import pandas as pd


# In[1000]:


data_costumer = pd.read_csv(r"C:\Users\Utilizador\Desktop\lab-customer-analysis-round-1\files_for_lab\csv_files\file1.csv")
data_costumer


# In[1001]:


data_costumer_2 = pd.read_csv(r"C:\Users\Utilizador\Desktop\lab-customer-analysis-round-1\files_for_lab\csv_files\file2.csv")
data_costumer_2


# In[1002]:


data_costumer_3 = pd.read_csv(r"C:\Users\Utilizador\Desktop\lab-customer-analysis-round-1\files_for_lab\csv_files\file3.csv")
data_costumer_3


# In[1003]:


data_costumer.shape


# In[1004]:


data_costumer_2.shape


# In[1005]:


data_costumer_3.shape


# In[1006]:


cols = []
for i in range(len(data_costumer.columns)): 
    cols.append(data_costumer.columns[i].lower().replace(' ', '_'))
data_costumer.columns = cols
data_costumer


# In[1007]:


cols = []
for i in range(len(data_costumer_2.columns)): 
    cols.append(data_costumer_2.columns[i].lower().replace(' ', '_'))
data_costumer_2.columns = cols
data_costumer_2


# In[1008]:


cols = []
for i in range(len(data_costumer_3.columns)): 
    cols.append(data_costumer_3.columns[i].lower().replace(' ', '_'))
data_costumer_3.columns = cols
data_costumer_3


# In[1009]:


data_costumer = data_costumer.rename(columns={ 'st':'state'})
data_costumer


# In[1010]:


data_costumer_2 = data_costumer_2.rename(columns={ 'st':'state'})
data_costumer_2


# In[1011]:


data_costumer


# In[1012]:


data_costumer_2


# In[1013]:


data_costumer_3


# In[1014]:


df1 = data_costumer.loc[:]
df2 = data_costumer_2.loc[:]
df3 = data_costumer_3.loc[:]
data_costumer = pd.concat([df1,df2,df3], axis = 0)
data_costumer


# In[1015]:


data_costumer.dtypes


# In[1016]:


data_costumer = data_costumer.drop(["education"], axis = 1)
data_costumer


# In[1017]:


data_costumer = data_costumer.drop(["number_of_open_complaints"], axis = 1)
data_costumer


# In[1038]:


data_costumer["customer_lifetime_value"] = pd.to_numeric(data_costumer["customer_lifetime_value"],errors="coerce") * 100


# In[1039]:


data_costumer


# In[1040]:


data_costumer.duplicated()


# In[1041]:


data_costumer[data_costumer.duplicated()]


# In[1042]:


data_costumer = data_costumer.drop_duplicates()
data_costumer


# In[1043]:


filtered_data = data_costumer[data_costumer['income'] <= 0]
filtered_data


# In[1044]:


data_costumer


# In[ ]:





# In[ ]:




