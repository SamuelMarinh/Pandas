import pandas as pd
import numpy as np

# DataFrame
datas = pd.date_range('20190101', periods = 60, freq="D")
df = pd.DataFrame(np.random.randn(60,5), index = datas, columns = list("ABCDE"))

print(f'\nPrimeiras 5 linhas do DataFrame:\n{df.head(5)}\n')  

# Adicionando uma nova coluna 'F', com a lógica de quais os valores da coluna A, são maiores que 0
df['F'] = df.A[df.A > 0]
print(f'\nAdicionando nova coluna "F", Se os valores de A < 0, vai assumir valor Nulo\n{df.head(5)}\n')  

# Função Copy, para fazer uma cópia da função
df_teste_1 = df.copy()
df_teste_2 = df.copy()
df_teste_3 = df.copy()
print(f'\nCriando Três Cópias do Data frame para estudo!!\n') 

# Remover os valores Nulos com Dropna()
df_removido = df_teste_1.dropna()
print(f'\nRemoção dos valores Nulos com dropna():\n{df_removido.head(5)}\n') 

# Na coluna 'F' usando a função fillna substitua os valores nulos pela Média da coluna 'A'
df_adicionado = df_teste_2.fillna(np.mean(df_teste_2.A))
print(f'\nSubstituição dos valores nulos pela média da coluna "A" com fillna:\n{df_adicionado.head(5)}\n') 

# Trocando o valor nulo por 1800
df_numeros = df_teste_3.fillna(value=1800)
print(f'\nSubstituindo os valores nulos por 1800 com fillna:\n{df_numeros.head(5)}\n') 

# Prints interessantes
print(f'\nTamanho do DataFrame com remoção:\n{df_removido.shape}')  
print(f'\nTamanho do DataFrame com média adicionada:\n{df_adicionado.shape}')  
print(f'\nTamanho do DataFrame com valos substituidos:\n{df_numeros.shape}')  
print(f'\nTamanho do DataFrame Original:\n{df.shape}\n')  
