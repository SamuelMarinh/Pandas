import pandas as pd

# Cadastro da loja A com ID,NOME,IDADE e CEP
cda = {'Id': ['AA2930','BB4563','CC2139','DE2521','GT3462','HH1158'],
              'Nome': ['Victor', 'Amanda', 'Bruna', 'Carlos', 'Ricardo', 'Maria'],
              'Idade': [20,35,40,54,30,27],
              'CEP':['00092-029','11111-111','22222-888','00000-999','88888-111','77777-666']}

cda = pd.DataFrame(cda, columns = ['Id', 'Nome', 'Idade', 'CEP'])
print(f'\nLoja A:\n{cda}\n')

# Cadastro da loja B com ID,NOME,IDADE e CEP
cdb = {'Id': ['CC9999','EF4488','DD9999','GT3462','HH1158'],
              'Nome': ['Marcos', 'Patricia', 'Ericka', 'Ricardo','Maria'],
              'Idade': [19,30,22,30,27],
              'CEP':['00092-029','11111-111','11111-888','88888-111','77777-666']}

cdb = pd.DataFrame(cdb, columns = ['Id', 'Nome', 'Idade', 'CEP'])
print(f'\nLoja B:\n{cdb}\n')

# Registro de Compras de todas as unidades
cp = {'Id': ['AA2930','EF4488','CC2139','EF4488','CC9999','AA2940','HH1158','HH1158'],
           'Data': ['2019-01-01','2019-01-30','2019-01-30','2019-02-01','2019-02-20','2019-03-15','2019-04-01','2019-04-10'],
           'Valor': [200,100,40,150,300,25,40,500]}

cp = pd.DataFrame(cp, columns = ['Id', 'Data', 'Valor'])
print(f'\nRegistro de compras:\n{cp}\n')

