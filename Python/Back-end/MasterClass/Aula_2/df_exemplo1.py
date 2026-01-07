import pandas as pd;
import numpy as np;

# Criação de um DataFrame de exempo
df = pd.DataFrame({
    'nome': ["Ana", "Bruno", "Carlos", "Daniele", "Val"],  
    'salario': [4000, np.nan, 5000, np.nan, 100000]
});

# Calcula e arredonda a media dos salarios e coloca nos valores nulos a media
df['media_salario'] = df['salario'].fillna(df['salario'].mean().round(2));

# Calcula a mediana
df['mediana_salario'] = df['salario'].fillna(df['salario'].median());

print(df.head());
# media_salarios