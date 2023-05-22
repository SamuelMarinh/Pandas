import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Definindo o Dataframe
df = pd.read_csv("train.csv")
print(f'\nDataFrame:\n{df}\n')

# Definindo o Dataframe
df = pd.read_csv("train.csv")
print(f'\nDataFrame:\n{df}\n')

# 5 primeiras linhas do Dataframe
print(f'\nDataFrame:\n{df.head(5)}\n')

# Definindo o tamanho da "pagina" plot.
plt.rcParams['figure.figsize'] = (20,7)

plt.plot(df.Age, '*-r')
plt.xlabel('Passageiros', size = 14 )
plt.ylabel('Idade', size = 18)
plt.show()

# Plotando gráfico de linhas 
df.Age.plot()
plt.xlabel('Passageiros', size = 14 )
plt.ylabel('Idade', size = 18)
plt.show()

# Plotando tudo
df.plot()
plt.show()

# Scatter plot, grafíco de dispersção dos crias
plt.scatter(df.PassengerId, df.Age)
plt.xlabel('Passageiros', size = 14 )
plt.ylabel('Idade', size = 18)
plt.show()

# Gráfico de histograma
print(f'\nDescribe\n{df.describe()}\n')
print(f'\nGráfico de histograma das idades:\n')

df.Age.hist()
plt.xlabel('Passageiros', size = 14 )
plt.ylabel('Frequencia de idades', size = 18)
plt.show()

