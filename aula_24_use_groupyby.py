import pandas as pd
import numpy as np

df = pd.DataFrame({'A': ['verdadeiro', 'falso', 'verdadeiro', 'falso','verdadeiro', 'falso', 'verdadeiro', 'falso'],
                  'B': ['um','um','dois','tres','dois','dois','um','tres'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)})

print(f'\nDados:\n{df}\n')

# Soma da categoria A
soma = df.groupby(['A']).mean(numeric_only=True)
print(f'\nSoma da Categoria A:\n{soma}\n')

# Média da categoria B
media = df.groupby(['B']).mean(numeric_only=True)
print(f'\nMédia da Categoria B:\n{media}\n')
