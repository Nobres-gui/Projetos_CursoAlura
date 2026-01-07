import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;
import plotly.express as px;


# Pega uma base de dados de um link (nesse caso do github)
# df = DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv");    

# Lê a base de dados inteira 
print(df.head());

# Entende informações gerais do arquivo
df.info();

# Descreve melhor o banco de dados
print((df.describe()));

# Traz a quantidade de linhas e colunas do arquivo
linhas, colunas = df.shape[0], df.shape[1];
print(f"Linhas: {linhas} \nColunas: {colunas}");

nome_colunas_en = df.columns;
print(nome_colunas_en);

renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato', 
    'job_title': 'cargo',
    'salary': 'salario', 
    'salary_currency': 'moeda', 
    'salary_in_usd': 'usd', 
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto', 
    'company_location': 'empresa', 
    'company_size': 'tamanho_empresa'
};

df.rename(columns=renomear_colunas, inplace=True);
nome_colunas_pt = df.columns;
print(nome_colunas_pt);

# Analisa qual a frequencia de cada categoria dentro da dataframe
categoria_senioridade = df["senioridade"].value_counts();
print(categoria_senioridade);

senioridade = {
    "SE": "Sênior",
    "MI": "Pleno",
    "EN": "júnior",
    "EX": "Executivo"
}

df['senioridade'] = df['senioridade'].replace(senioridade);
print(df['senioridade'].value_counts())

categoria_contrato = df["contrato"].value_counts();
print(categoria_contrato);

contrato = {
    "FT": "Integral",
    "PT": "Parcial",
    "FL": "Freelance",
    "CT": "Contrato"
}

df['contrato'] = df['contrato'].replace(contrato);
print(df['contrato'].value_counts())

categoria_tamanho_empresa = df["tamanho_empresa"].value_counts();
print(categoria_tamanho_empresa);

tamanho_empresa = {
    "S": "Pequena",
    "M": "Média",
    "L": "Grande"
}

df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa);
print(df['tamanho_empresa'].value_counts())

categoria_remoto = df["remoto"].value_counts();
print(categoria_remoto);

remoto = {
    0: "Presencial",
    50: "Híbrido",
    100: "Remoto"
}

df['remoto'] = df['remoto'].replace(remoto);
print(df['remoto'].value_counts())


print(df.describe(include="object"));

print(df.isnull());
print(df.isnull().sum());

# Traz valores unicos dentro da coluna em especifico
ano = df["ano"].unique();
print(ano);

# Mostra apenas os dados onde em alguma coluna há valores nulos
valores_nulos = df[df.isnull().any(axis=1)];
print(valores_nulos);

df_limpo = df.dropna();

print(df_limpo.isnull().sum());
print(df_limpo.info());

#Converte o tipo de dado do vlaor
df_limpo = df_limpo.assign(ano =df_limpo['ano'].astype('int64')); # type: ignore

print(df_limpo.head());
# plt.show();

# cria um gráfico 
df_limpo['senioridade'].value_counts().plot(kind='bar', title='Distribuição de senioridade');
# plt.show();

sns.barplot(data=df_limpo, x='senioridade', y='usd');
# plt.show();

# Configura os dados para mostrar de forma decrescente
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index;

plt.figure(figsize=(8,5));
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem);
plt.title("Salário por Senioridade");
plt.xlabel("Senioridade");
plt.ylabel("Salário Médio Anual(USD)");
# plt.show();

plt.figure(figsize=(8,4));
sns.histplot( df_limpo['usd'], bins=50, kde=True) #type: ignore
plt.title("Distribuição dos Salários");
plt.xlabel("Salário (USD)");
plt.ylabel("Frequência");
# plt.show();

plt.figure(figsize=(8,5));
sns.boxplot(x=df_limpo['usd']);
plt.title('Distribuição dos Salários anuais');
plt.xlabel('Salário em USD');
# plt.show();

ordem_senioridade = ['júnior', 'Pleno', 'Sênior', 'Executivo']
plt.figure(figsize=(8,5));
#Adiciona cor nos dados do grafico
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade');
plt.title('Distribuição salárial por senioridade');
plt.xlabel('Salário em USD');
plt.ylabel('Senioridade');
# plt.show();

senioridade_media_salarial = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index();

figBar = px.bar(
    senioridade_media_salarial,
    x='senioridade',
    y='usd',
    labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial ANUAL (USD)'}
)

figBar.show();

remoto_contagem = df_limpo['remoto'].value_counts().reset_index();
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

figPizza = px.pie(
    remoto_contagem,
    names='tipo_trabalho',
    values='quantidade',
    title='Proporção dos tipos de trabalho'
)

figPizza.show();

figRosca = px.pie(
    remoto_contagem,
    names='tipo_trabalho',
    values='quantidade',
    title='Proporção dos tipos de trabalho',
    hole=0.5
)
figRosca.update_traces(textinfo='percent+label')
figRosca.show();