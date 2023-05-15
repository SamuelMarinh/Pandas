import pandas as pd 
import numpy as np

#Definindo o DataFrame
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2,1: 4,2: 6}})

print(f'\nDados:\n{df}\n')

#Usando a função melt para combinar A com B numa tabela
Tabela_1 = pd.melt(df, id_vars=['A'],value_vars=['B'])
print(f'\nFunção Melt:\n{Tabela_1}\n')

#Usando a função melt para combinar A com B e Cnuma tabela
Tabela_2 = pd.melt(df, id_vars=['A'],value_vars=['B', 'C'])
print(f'\nFunção Melt:\n{Tabela_2}\n')

#Alterar o nome da tabela
rename = pd.melt(df, id_vars=['A'],value_vars=['B','C'], var_name='Loja',value_name='Quantidade')
print(f'\nAlteração do nome das colunas:\n{rename}\n')  