#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods = 6)
df = pd.DataFrame(np.random.randn(6,4), index=datas, columns=['Var_A','Var_B','Var_C','Var_D'])


# In[4]:


df2 = pd.DataFrame({"A":7,
                   "B": pd.Timestamp('20190101'),
                   "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                    "D": np.array([3] * 4, dtype='int32'),
                    "E": pd.Categorical(["test","train","test","train"]),
                    "F": 'Python'
                   })


# In[7]:


df.dtypes


# In[10]:


df2.dtypes


# In[11]:


df2.describe()


# In[14]:


df1 = df.reindex(index=datas[0:4],columns=list(df.columns) + ['Var_E'])


# In[15]:


df1


# In[16]:


df1.loc[data[0]:datas[1], 'Var_E'] = 77


# In[17]:


df1


# In[18]:


df1.describe()


# In[22]:


datas = pd.date_range('20190101', periods = 60, freq="D")
df = pd.DataFrame(np.random.randn(60,5), index = datas, columns = list("ABCDE"))


# In[23]:


df.head(3)


# In[24]:


df['F'] = df.A[df.A > 0]


# In[25]:


df.head(3)


# In[31]:


df2 = df.copy()


# In[33]:


df2.dropna().shape


# In[37]:


df3 = df.copy()


# In[38]:


df3.head(3)


# In[39]:


df2.F.fillna(np.mean(df3.A))


# In[40]:


df4 = df.copy()


# In[42]:


df4.fillna(value = 77777)


# In[50]:


df2 = pd.DataFrame({"A":7,
                   "B": pd.Timestamp('20190101'),
                   "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                    "D": np.array([3] * 4, dtype='int32'),
                    "E": pd.Categorical(["test","train","test","train"]),
                    "F": 'Python',
                    "G": [2,2,4,4],
                    "H": [np.nan,2,4,np.nan]
                   })


# In[51]:


df2.nunique()


# In[54]:


df2.nunique(dropna=False)


# In[55]:


df2.nunique(axis=1,dropna=False)


# In[ ]:




