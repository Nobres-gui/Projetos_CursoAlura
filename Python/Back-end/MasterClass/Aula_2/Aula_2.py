import pandas as pd;

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv");

print(df.isnull());
print(df.isnull().sum());

# Traz valores unicos dentro da coluna em especifico
ano = df["work_year"].unique();
print(ano);

# Mostra apenas os dados onde em alguma coluna há valores nulos
valores_nulos = df[df.isnull().any(axis=1)];
print(valores_nulos);

df_limpo = df.dropna();

print(df_limpo.isnull().sum());
print(df_limpo.info());

#Converte o tipo de dado do vlaor
df_limpo = df_limpo.assign(work_year =df_limpo['work_year'].astype('int64')); # type: ignore

print(df_limpo.head());
print(df_limpo.info());