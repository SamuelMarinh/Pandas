#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


datas = pd.date_range('20200101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=datas,columns=['Var_A','Var_B','Var_C','Var_D'])


# In[5]:


df


# In[6]:


df.shape


# In[8]:


dft = df.T


# In[9]:


dft.shape


# In[10]:


dft.values


# In[11]:


np.size(dft)


# In[13]:


np.size(df.values)


# In[14]:


v = dft.values


# In[15]:


v.reshape((2,12))


# In[28]:


Dia = pd.date_range(start='20190101', periods=12)
Dia


# In[17]:


Pessoa = ['George', 'Victor', 'Lucas']


# In[18]:


np.random.choice(Pessoa)


# In[22]:


Nome = []
Gasto = []
for i in range(12):
    Nome.append(np.random.choice(Pessoa))
    Gasto.append(np.round(np.random.rand()*100,2))
Nome


# In[23]:


Gasto


# In[30]:


df = pd.DataFrame({'Dia':dias, 'Nome':Nome, 'Gasto':Gasto})


# In[25]:


df


# In[34]:


df.pivot(index='Dia',columns='Nome',values='Gasto')


# In[ ]:


df


# In[37]:


Carros = [7,4,3,2,8]
dias = pd.date_range('20190101','20190101',periods=5)
vendedor = ['George','Vagner','Pedro','Vagner','George']
df = pd.DataFrame({'Vendas':Carros, 'Data':dias, 'Vendedor':vendedor})
df


# In[38]:


pd.pivot(df, index='Data', columns='Vendedor', values='Vendas')


# In[42]:


pd.pivot_table(df, index='Data', columns='Vendedor', values='Vendas',aggfunc=sum)


# In[43]:


df2 = pd.read_csv("https://cdncontribute.geeksforgeeks.org/wp-content/uploads/nba.csv")


# In[45]:


df2.head(4)


# In[47]:


df2.shape


# In[48]:


stack_df2 = df2.stack()


# In[49]:


stack_df2


# In[51]:


udf2 = stack_df2.unstack()


# In[52]:


udf2.head(2)


# In[53]:


df3 = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2,1: 4,2: 6}})


# In[54]:


df3


# In[57]:


pd.melt(df3, id_vars=['A'],value_vars=['B'])


# In[58]:


pd.melt(df3, id_vars=['A'],value_vars=['B','C'])


# In[59]:


pd.melt(df3, id_vars=['A'],value_vars=['B','C'], var_name='VarTeste',value_name='Nome do Valor')


# In[60]:


data = {
    "localizacao":['CidadeA', 'CidadeB'],
    "Temperatura": ["Prevista", "Atual"],
    "Set-2019":[30,32],
    "Out-2019":[45,43],
    "Nov-2019":[24,22],
}
print(data)


# In[62]:


df5 = pd.DataFrame(data, columns=['localizacao','Temperatura','Set-2019','Out-2019','Nov-2019'])
df5


# In[65]:


data


# In[64]:


df2 = pd.melt(df5, id_vars=["localizacao", "Temperatura"], var_name="Date", value_name="Value")
print(df2)


# In[71]:


datas = pd.date_range('20180101', periods=600,freq="D")
DF = pd.DataFrame(np.random.randn(600,5), index = datas, columns = list("ABCDE"))


# In[80]:


DF.loc[:,['B','C','D']]



# In[81]:


DF.loc['20180301':'20180917',['A','E']]


# In[82]:


F = len(DF.loc['20180301':'20180917',['A','E']])
F


# In[85]:


DF.iloc[1]


# In[88]:


DF.iloc[2:8,0:2]


# In[89]:


DF.iloc[[1,5,6],[0,3]]


# In[91]:


DF.iloc[1:3,:]


# In[92]:


DF.A


# In[98]:


DF[DF.A > 0]


# In[102]:


DF[DF>0]


# In[ ]:





# In[ ]:




