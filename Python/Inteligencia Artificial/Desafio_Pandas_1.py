import pandas as pd;
from google import genai;
from dotenv import load_dotenv;
import os;

load_dotenv();

api_key = os.environ.get("GOOGLE_API_KEY2");

if api_key is None:
    print("Erro: A chave não foi encontrada no .env ou nas variáveis de ambiente.")
else:
    print(f"Chave carregada com sucesso")
        
client = genai.Client(api_key = api_key);

lista_perguntas = [
    "De que é feito o Sol?",
    "De que é feito o planeta Saturno?",
    "Qual é a galáxia mais antiga já encontrada?",
    "Qual é a maior estrela já encontrada?",
    "Qual é a estrela mais próxima do Sol?"
    ];

respostas_perguntas = [];

def escrever_arquivo(linha):
    with open("Desafio Perguntas.txt", "w", encoding="utf-8") as arquivo:
        for linha in lista_perguntas:
            arquivo.write(linha + "\n");

escrever_arquivo(lista_perguntas);

def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            perguntas_arquivo.append(linha.strip());

perguntas_arquivo = [];

ler_arquivo("C:\\Users\\guilh\\Downloads\\Alura\\curso_alura\\Python\\Desafio Perguntas.txt");
print(perguntas_arquivo);

for pergunta in perguntas_arquivo:
    response = client.models.generate_content( model="gemini-2.5-flash-lite", contents=f"responda a pergunta de forma resumida e objetiva: {pergunta}");
    respostas_perguntas.append({"pergunta": pergunta, "resposta": response.text});

# def criar_arquivo_csv():
#     with open("Respostas Desafio.csv", "w", encoding="utf-8") as arquivo_csv:
#         arquivo_csv.write("Pergunta,Resposta\n");
#         for item in respostas_perguntas:
#             arquivo_csv.write(f'"{item["pergunta"]}","{item["resposta"]}"\n');
        
# criar_arquivo_csv();

dataFrame = pd.DataFrame(respostas_perguntas);
dataFrame.to_csv("Respostas Desafio.csv", index=False, encoding="utf-8");
                           
df = pd.read_csv('C:\\Users\\guilh\\Downloads\\Alura\\curso_alura\\Python\\Respostas Desafio.csv');
print(df.head());


