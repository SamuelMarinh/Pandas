import pandas as pd
import numpy as np

# Caminho do arquivo Excel
caminho_arquivo = 'C:/Users/samuel.marinho/Desktop/Python/Pandas/nba.csv'

# Leitura do arquivo em Excel
dados = pd.read_csv(caminho_arquivo, sep=',')
print(f'\nPrimeiras 5 linhas:\n{dados.head(5)}\n')
print(f'\nDimensão dos dados:\n{dados.shape}\n')

# Fazendo um empilhamento de coluna para linha
empilha_stack = dados.stack()
print(f'\nUsando a função Stack para empilhamento:\n{empilha_stack}\n')

# Fazendo um empilhamento de coluna para linha
empilha_stack = dados.stack()
print(f'\nUsando a função Stack para empilhamento:\n{empilha_stack}\n')

# Voltando o arquivo para como estava
Volta_pra_mim = empilha_stack.unstack()
print(f'\nUsando a função unstack para voltar o arquiv para o formato anterior:\n{Volta_pra_mim}\n')