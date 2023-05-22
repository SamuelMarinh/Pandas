import pandas as pd
import numpy as np

# DataFrame
df = pd.DataFrame({'A': ['verdadeiro', 'falso', 'verdadeiro', 'falso','verdadeiro', 'falso', 'verdadeiro', 'falso'],
                  'B': ['um','um','dois','tres','dois','dois','um','tres'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)})

print(f'\nPrimeiras 5 linhas do DataFrame:\n{df.head(5)}\n')

# Ordenando os itenss
ORD = df.sort_values(by='C', ascending=False)
print(f'\nOrdenando os itens de forma decrescente mediante a coluna "C":\n{ORD}\n')
