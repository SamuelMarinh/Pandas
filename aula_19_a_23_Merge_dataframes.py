import pandas as pd

# Cadastro da loja A com ID,NOME,IDADE e CEP
Cadastro_loja_A = {'Id': ['AA2930','BB4563','CC2139','DE2521','GT3462','HH1158'],
              'Nome': ['Victor', 'Amanda', 'Bruna', 'Carlos', 'Ricardo', 'Maria'],
              'Idade': [20,35,40,54,30,27],
              'CEP':['00092-029','11111-111','22222-888','00000-999','88888-111','77777-666']}

Cadastro_loja_A = pd.DataFrame(Cadastro_loja_A, columns = ['Id', 'Nome', 'Idade', 'CEP'])
print(f'\nLoja A:\n{Cadastro_loja_A}\n')


# Cadastro da loja B com ID,NOME,IDADE e CEP
Cadastro_loja_B = {'Id': ['CC9999','EF4488','DD9999','GT3462','HH1158'],
              'Nome': ['Marcos', 'Patricia', 'Ericka', 'Ricardo','Maria'],
              'Idade': [19,30,22,30,27],
              'CEP':['00092-029','11111-111','11111-888','88888-111','77777-666']}

Cadastro_loja_B = pd.DataFrame(Cadastro_loja_B, columns = ['Id', 'Nome', 'Idade', 'CEP'])
print(f'\nLoja B:\n{Cadastro_loja_B}\n')


# Registro de Compras de todas as unidades
Compras = {'Id': ['AA2930','EF4488','CC2139','EF4488','CC9999','AA2940','HH1158','HH1158'],
           'Data': ['2019-01-01','2019-01-30','2019-01-30','2019-02-01','2019-02-20','2019-03-15','2019-04-01','2019-04-10'],
           'Valor': [200,100,40,150,300,25,40,500]}

Compras = pd.DataFrame(Compras, columns = ['Id', 'Data', 'Valor'])
print(f'\nRegistro de compras:\n{Compras}\n')


#Inner join, para ver quais clientes estão em ambas as lojas
merge_a_b = pd.merge(Cadastro_loja_A,Cadastro_loja_B, on=['Id'], how="inner", suffixes=('_A', '_B'))
print(f'\nClientes que estão na loja A e na loja B:\n{merge_a_b}\n')


#Full join, daria para usar o concat, mas os dados poderiam se repetir
conc = pd.concat([Cadastro_loja_A,Cadastro_loja_B],ignore_index=True)
print(f'\nConcatenando:\n{conc}\n\nNota-se que Maria e Ricardo se repetem!!\n')

cliente_unicos = conc.drop_duplicates(subset='Id')
print(f'\nDados tratados:\n{cliente_unicos}\n')


#Left join, Quais clientes fizeram uma compra e estão cadastrados na loja A
merge_compras = pd.merge(Cadastro_loja_A,Compras, on=['Id'], how='left', suffixes=('_A', '_B'))
print(f'\nClientes cadastrados em A que fizeram uma compra:\n{merge_compras }\n')

merge_tratado = merge_compras.groupby(['Id', 'Nome'])['Valor'].sum()
print(f'\nMerge tratado com groupby:\n{merge_tratado}\n')
