import pandas as pd

# Primeiro DataFrame com índice 0, 1, 2, 3
df1 = pd.DataFrame({'A' : ['A0', 'A1', 'A2', 'A3'],
                    'B' : ['B0', 'B1', 'B2', 'B3'],
                    'C' : ['C0', 'C1', 'C2', 'C3'],
                    'D' : ['D0', 'D1', 'D2', 'D3']}, index=[0,1,2,3])

# Segundo DataFrame com índice 4, 5, 6, 7
df2 = pd.DataFrame({'A' : ['A4', 'A5', 'A6', 'A7'],
                    'B' : ['B4', 'B5', 'B6', 'B7'],
                    'C' : ['C4', 'C5', 'C6', 'C7'],
                    'D' : ['D4', 'D5', 'D6', 'D7']}, index=[4,5,6,7])

# Terceiro DataFrame com índice 8, 9, 10, 11
df3 = pd.DataFrame({'A' : ['A8', 'A9', 'A10', 'A11'],
                    'B' : ['B8', 'B9', 'B10', 'B11'],
                    'C' : ['C8', 'C9', 'C10', 'C11'],
                    'D' : ['D8', 'D9', 'D10', 'D11']}, index=[0,1,2,3])

# Exibir os DataFrames
print(f"\nPrimeiro DataFrame:\n{df1}\n")
print(f"\nSegundo DataFrame:\n{df2}\n")
print(f"\nTerceiro DataFrame:\n{df3}\n")

# Concatenando os DataFrames
frames = [df1, df2, df3]
grupo = pd.concat(frames)
print(f"\nDataFrame Concatenado:\n{grupo}\n")

# Definindo parametros para o grupo
grupo_n = ['g1', 'g2', 'g3']
grupo_df = pd.concat(frames, keys=grupo_n)
print(f"\nGrupo atualizado:\n{grupo_df}\n")

# Extraindo apenas a Coluna B
col_b = grupo_df['B']
print(f"\nColuna B:\n{col_b}\n")

# Extraindo apenas a grupo 3
grupo_3 = grupo_df.loc['g3']
print(f"\nGrupo 3:\n{grupo_3}\n")