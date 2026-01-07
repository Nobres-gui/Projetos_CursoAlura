import pandas as pd;
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
    "Ex": "Executivo"
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