import pandas as pd
import numpy as np

# DataFrame
df = pd.DataFrame({"A":7,
                   "B": pd.Timestamp('20190101'),
                   "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                    "D": np.array([3] * 4, dtype='int32'),
                    "E": pd.Categorical(["test","train","test","train"]),
                    "F": 'Python',
                    "G": [2,2,4,4],
                    "H": [np.nan,2,4,np.nan]
                   })

print(f'\nPrimeiras 5 linhas do DataFrame:\n{df.head(5)}\n')

# Contar quantos numeros distintos tem nas colunas
contagem = df.nunique()
print(f'\nNúmeros distintos nas colunas:\n{contagem}\n')

# Para contabilizar o valor Nulo dropna = False
contagem_nula = df.nunique(dropna=False)
print(f'\nNúmeros distintos nas colunas com Nulos:\n{contagem_nula}\n')

# Função axis = 1 para contar quantas vezes os numeros se repetem por linha
contagem_value = df.nunique(axis=1 ,dropna=False)
print(f'\nRepeticição de números por linha:\n{contagem_value}\n')
