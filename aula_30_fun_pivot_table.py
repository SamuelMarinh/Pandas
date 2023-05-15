import pandas as pd
import numpy as np

#Lista de Carros
Carros = [1, 3, 4, 5, 9, 7]

# Análise com dados aleatórios
dias = pd.date_range('20190101', '20190101', periods=6)

#Lista de vendedores
Vendedores = ['Samuel', 'Daniel', 'Codeco', 'Gabi', 'Daniel', 'Samuel']

#Definindo o DataFrame  
df = pd.DataFrame({'Vendas':Carros, 'Data':dias, 'Vendedores':Vendedores})
print(f'\nDataFrame: {df}\n')

#Pega a média aggfun=(''), muda esse calculo
mudanca_pivot = pd.pivot_table(df, index='Data', columns='Vendedores', values='Vendas', aggfunc='sum')
print(f'\nTabela:\n{mudanca_pivot}\n')