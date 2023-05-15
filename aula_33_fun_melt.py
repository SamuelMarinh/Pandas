import pandas as pd 
import numpy as np

#Definindo o DataFrame
data = {"localizacao":['CidadeA', 'CidadeB'],
        "Temperatura": ["Prevista", "Atual"],
        "Set-2019":[30,32],
        "Out-2019":[45,43],
        "Nov-2019":[24,22],
}
print(f'\nDados:\n{data}\n')    

#Definindo o DataFrame
df1 = pd.DataFrame(data, columns=['localizacao','Temperatura','Set-2019','Out-2019','Nov-2019'])
print(f'\nDataFrame:\n{df1}\n')   

#Tratamento com melt
df2 = pd.melt(df1, id_vars=["localizacao", "Temperatura"], var_name="Date", value_name="Value")
print(f'\nDataFrame com melt:\n{df2}\n')   