import pandas as pd
import numpy as np

# Análise com dados aleatórios
dias = pd.date_range('20190101', periods=12)
print(f'\nBase de dados obtidas:\n{dias}\n')

#Lista de nomes com um random, para escolher de forma aleatória
pessoas = ['Samuel', 'Daniel', 'Codeco', 'Gabi', 'Elisia']
np.random.choice(pessoas)

#Definindo listas vazias e um for para preencher o mesmo
Nome = []
Gastos = []
for i in range(12):
    Nome.append(np.random.choice(pessoas))
    Gastos.append(np.round(np.random.rand()*100,2))

print(f'\nLista de pessoas: {Nome}\n')
print(f'\nLista de Gastos: {Gastos}\n')

#Definindo o dataframe
df = pd.DataFrame({'Dia':dias, 'Nome':Nome, 'Gastos':Gastos})
print(f'\nDataFrame: {df}\n')

#Nome da pessoa com seus gastos respectivos
mudanca_pivot = df.pivot(index='Dia', columns='Nome', values='Gastos')
mudanca_pivot.fillna(0, inplace=True)
print(f'\nGasto de pessoa por dia:\n{mudanca_pivot}\n')