import pandas as pd;
import numpy as np;

# Criação de um DataFrame de exempo
df = pd.DataFrame({
    'dia': ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"],  
    'temperatura': [30, np.nan, np.nan, 38, 27, 21, 18]
});

#Completa o números nulos com o valor do dado anterior
df['preenchido_ffill'] = df['temperatura'].ffill();

#Completa o números nulos com o valor do dado posterior
df['preenchido_bfill'] = df['temperatura'].bfill();

print(df);