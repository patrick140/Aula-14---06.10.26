import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.loureiro\Downloads\funcionarios.csv")

#print(df.loc[0:5, 'id':'departamento'])

#print(df.iloc[0:5, 0:3])

salario = df.query("salario > 3000 and ativo == True")

SalarioNome = df[["nome", "salario"]]

print(salario)
print(type(SalarioNome))
print(df.info())

