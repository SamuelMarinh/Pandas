import pandas as pd
import numpy as np

# Criando os dados
data = pd.date_range('20180101', periods=600,freq="D")
print(f'\nDados:\n{data}\n')    

# Definindo o DataFrame
df = pd.DataFrame(np.random.randn(600,5), index = data, columns = list("ABCDE"))
print(f'\nDataFrame:\n{df}\n')   

# Visualizar 3 primeiras linhas
print(f'\n3 primeiras linhas:\n{df.head(3)}\n')

# Visualizar 3 ultimas linhas
print(f'\n3 ultimas linhas:\n{df.tail(3)}\n')

# Visualizar as linhas da coluna D e suas primeiras 5 linhas
print(f'\n5 Primeias linhas da Coluna D:\n{df["D"].head(5)}\n')

# Selecionar todas as linhas da coluna A, B e C usando a função LOC
print(f'\nTabela das colunas A,B e C:\n{df.loc[:,["A","B","C"]]}\n')

# Selecionar um intervalo de datas e duas colunas ja pré selecionadas, com a função LOC
valor = df.loc["20180301":"20180917",["A","E"]]
print(f'\nValores de A e E entre 20180301 e 20180917:\n{valor}\n')

# Quantidade de dados que o arquivo anterior possui usando len
print(f'\nQuantidade de dados:\n{len(valor)}\n')

# Definindo um filtro de itens com valor maior que 2 na Coluna A
print(f'\nQuantidade de dados:\n{df[df.A > 2 ]}\n')

