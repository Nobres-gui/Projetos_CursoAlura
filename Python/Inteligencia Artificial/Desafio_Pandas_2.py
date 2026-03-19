import pandas as pd;
from dotenv import load_dotenv;
import os;
from google import genai;

load_dotenv();
api_key = os.environ.get("GOOGLE_API_KEY");

if api_key is None:
    print("Erro: A chave não foi encontrada no .env ou nas variáveis de ambiente.");
else:
    print(f"Chave carregada com sucesso");

client = genai.Client(api_key = api_key);

df_reviews = pd.read_csv('C:\\Users\\guilh\\Downloads\\Alura\\curso_alura\\Python\\Inteligencia Artificial\\reviews.csv');

df_reviews_text = df_reviews["reviewText"];

lista_reviews_sentimento = [];

for review in df_reviews_text:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= f"Leia e interprete o sentimento de cada review classificando em positivo, negativo ou neutro: {review}"
        );
        lista_reviews_sentimento.append(response.text.lower()); # type: ignore
    except Exception as e:
        print(f"Erro ao processar a review. Erro: {e}")
        break;
    
print(f"Linhas no CSV: {len(df_reviews)}")
print(f"Itens na Lista: {len(lista_reviews_sentimento)}")
df_reviews["reviewFelings"] = lista_reviews_sentimento;

df_reviews_negativas = df_reviews[df_reviews["reviewFelings"] == "negativo"];

resenhas_negativas = df_reviews_negativas["reviewText"];
resenhas_negativas_unidas = "#####".join(resenhas_negativas);

categoryResponse = client.models.generate_content(
    model="gemini-2.5-flash",
    contents= f"""Você é um analista de dados. vou te passar muitas resenhas negativas de um produto separadas por '#####' , e quero que você encontre 5 categorias deiferentas para os tipos de reclamacoes. quero que você me retorne as 5 categorias.
    cada categoria dever ser definida por uma palavra ou termo curto.
    
    Aqui estão as resenhas negativas, {resenhas_negativas_unidas}"""
);

categorias_negativa = categoryResponse.text; # type: ignore
lista_categorias_negativas = categorias_negativa.split(sep=", "); # type: ignore