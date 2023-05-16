import pandas as pd
import numpy as np

datas = pd.date_range('20200101', periods = 6)
df = pd.DataFrame(np.random.randn(6,4), index=datas, columns=['Var_A','Var_B','Var_C','Var_D'])

df2 = pd.DataFrame({"A":7,
                    "B": pd.Timestamp('20190101'),
                    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
                    "D": np.array([3] * 4, dtype='int32'),
                    "E": pd.Categorical(["test","train","test","train"]),
                    "F": 'Python'})

print(df)