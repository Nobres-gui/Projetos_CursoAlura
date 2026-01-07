import pandas as pd;
import numpy as np;

# Criação de um DataFrame de exempo
df = pd.DataFrame({
    'nome': ["Ana", "Bruno", "Carlos", "Daniele", "Val"],  
    'cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Belém']
});

#Pega o valor nulo e coloca o que for delimitado na função fillna()
df['cidade_preenchida'] = df['cidade'].fillna("Não Informado");

print(df);