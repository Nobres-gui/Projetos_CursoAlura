import pandas as pd;
import numpy as np;

nomes_produtos = [f"Produto {i+1}" for i in range(50)];
categorias_produtos = np.random.choice(["Eletrônicos", "Livros", "Roupas", "Alimentos", "Brinquedos"], 50);
precos_produtos = np.random.uniform(10.0, 500.0, 50).round(2);
itens_vendidos = np.random.randint(1, 1000, 50);
avaliacoes_produtos = np.random.uniform(1.0, 5.0, 50).round(1);

# Criando o DataFrame
df_produtos = pd.DataFrame({
    "Nome do produto": nomes_produtos,
    "Categoria do produto": categorias_produtos,
    "Preço do produto": precos_produtos,
    "Itens vendidos": itens_vendidos,
    "Avaliação do produto": avaliacoes_produtos
})

#Mostra a coluna do DataFrame com base no Titulo dela
df_categoria = df_produtos["Categoria do produto"];

#Mostra a quantidade de linhas e colunas do DataFrame
df_shape = df_produtos.shape;

#Ver "Titulos" das colunas
df_titulos = df_produtos["Categoria do produto"].unique();

#Filtragem por preço menor que 100
df_preco_menor_100 = df_produtos[df_produtos["Preço do produto"] < 100]; 

#Filtragem por categoria "Eletrônicos"
df_eletronicos = df_produtos[df_produtos["Categoria do produto"] == "Eletrônicos"]; 

#Filtragem por avaliação maior ou igual a 4.5
df_avaliacao_maior_45 = df_produtos[df_produtos["Avaliação do produto"] >= 4.5]; 

#Filtragem por itens vendidos maior que 500
df_itens_vendidos_maior_500 = df_produtos[df_produtos["Itens vendidos"] > 500]; 

#ILOC
df_iloc = df_produtos.iloc[40:]; #Seleciona as linhas a partir do índice 40 até o final

#LOC
df_loc = df_produtos.loc[df_produtos["Nome do produto"] == "Produto 15", ["Preço do produto"]]; #Seleciona produtos com nome Produto 15, mostrando apenas o preço

df_nome_novo = df_produtos[df_produtos["Categoria do produto"] == "Brinquedos"];
df_produtos.loc[df_nome_novo.index, "Categoria do produto"] = "Infantis";


print(df_produtos["Categoria do produto"].unique());