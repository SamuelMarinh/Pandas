import pandas as pd
import numpy as np

# Lista já pre-definida e seu tipo
data = [7, 4, 2, np.nan, 6, 9]
series = pd.Series(data)
print(f'Lista estabelecida:\n{data}\n')
print(f'\nTipo dos dados:\n{type(series)}\n')

# Input do usuário
data = input("Digite a data no formato AAAA-MM-DD: ")
frequencia = input("Digite 'a' para ano, 'm' para mês e 'd' para dia: ")

# Condicional para frequência
if frequencia.lower() == 'a':
    periodo = int(input("Digite o período em anos que deseja analisar: "))
    datas = pd.date_range(data, periods=periodo, freq=frequencia)
    print(f'\nLista de datas:\n{datas}\n')

elif frequencia.lower() == 'm':
    periodo = int(input("Digite o período em meses que deseja analisar: "))
    datas = pd.date_range(data, periods=periodo, freq=frequencia)
    print(f'\nLista de datas:\n{datas}\n')

elif frequencia.lower() == 'd':
    periodo = int(input("Digite o período em dias que deseja analisar: "))
    datas = pd.date_range(data, periods=periodo, freq=frequencia)
    print(f'\nLista de datas:\n{datas}\n')

else:
    print('Favor digitar um dos caracteres mencionados!')

# Análise com dados aleatórios
df = pd.DataFrame(np.random.randn(periodo, 4), index=datas, columns=list("ABCD"))
print(f'\nBase de dados obtidas:\n{df}\n')

#Dimensionamento dos dodos
print(f'\nDimensão dos dados:\n{df.shape}\n')

#Visualizar 3 primeiras linhas
print(f'\n3 primeiras linhas:\n{df.head(3)}\n')

#Visualizar 3 ultimas linhas
print(f'\n3 ultimas linhas:\n{df.tail(3)}\n')

#Visualizar as colunas
print(f'\n3 ultimas linhas:\n{df.columns}\n')

#Visualizar o index
print(f'\n3 ultimas linhas:\n{df.index}\n')