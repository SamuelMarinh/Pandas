import pandas as pd
import numpy as np

# DataFrame
datas = pd.date_range('20200101', periods = 6)
df = pd.DataFrame(np.random.randn(6,4), index=datas, columns=['Var_A','Var_B','Var_C','Var_D'])

df2 = pd.DataFrame({"A":7,
                    "B": pd.Timestamp('20190101'),
                    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                    "D": np.array([3] * 4, dtype='int32'),
                    "E": pd.Categorical(["test","train","test","train"]),
                    "F": 'Python'})

print(f'\nPrimeiro Dataframe:\n{df}\n')  
print(f'\nSegundo Dataframe:\n{df2}\n')  

print(f'\nType do primeiro Dataframe:\n{df.dtypes}\n')  
print(f'\nType do segundo Dataframe:\n{df2.dtypes}\n')  

print(f'\nDescribe do primeiro Dataframe:\n{df.describe()}\n')  
print(f'\nDescribe do segundo Dataframe:\n{df2.describe()}\n')  

# Adicionando uma nova coluna 'E', selecionando as primeiras 4 datas
df1 = df.reindex(index=datas[0:4],columns=list(df.columns) + ['Var_E'])
print(f'\nAdicionando nova coluna e selecionando as 4 primeiras linhas:\n{df1}\n')  

# Adicionando o valor 100 nas linhas 1 e 2 na coluna 'E"
df1.loc[datas[0]:datas[1], 'Var_E'] = 100
print(f'\nAdicionando o valor 100 nas linhas 1 e 2 em "E":\n{df1}\n') 

print(f'\nType do Dataframe:\n{df1.dtypes}\n')  
print(f'\nDescribe do Dataframe:\n{df1.describe()}\n')  