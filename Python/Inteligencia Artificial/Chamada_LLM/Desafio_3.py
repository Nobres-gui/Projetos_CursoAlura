import pandas as pd;
from openai import OpenAI;
import json;

def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read();
    return conteudo;


texto = ler_arquivo('C:\\Users\\guilh\\Downloads\\Alura\\curso_alura\\Python\\Inteligencia Artificial\\Chamada_LLM\\Desafio_text.txt');


client = OpenAI(
    base_url="http://127.0.0.1:65000/v1",
    api_key="lm-studio"
);

resposta_ia = [];
for linha in texto.split('\n'):
    response = client.responses.create(
        model="google/gemma-3-1b",
        input=[
                    {"role": "system", "content": """ Leia todos os textos recebidos.
                    Cada linha possui o formato:

                    ID$usuario$texto_original

                    Tarefas:
                    1. Identifique o usuário
                    2. Preserve o texto original
                    3. Traduza o texto para português brasileiro
                    4. Classifique o sentimento como: positivo, negativo ou neutro
                    
                Retorne APENAS um JSON válido no formato:
                    {
                        "usuario": "...",
                        "resenha_original": "...",
                        "resenha_traduzida": "...",
                        "sentimento": "..."
                    }
                    """},
                    {"role": "user", "content": linha}
        ],
        temperature=0
    );
    resposta_ia.append(response.output_text.replace('\n', '').replace('```json', '').replace('```', ''));

def contar_sentimentos(respostas):
    sentimento_positivo = 0;
    sentimento_negativo = 0;
    sentimento_neutro = 0;

    for item in respostas:
        
        dados = json.loads(item);
        
        chave_json = list(dados.keys())[-1];
        valor_sentimento = dados[chave_json];
        
        
        match valor_sentimento:
            case "positivo":
                sentimento_positivo += 1;
            case "negativo":
                sentimento_negativo += 1;
            case "neutro":
                sentimento_neutro += 1;
    return sentimento_positivo, sentimento_negativo, sentimento_neutro;


string_resposta_ia =" ##### ".join(resposta_ia);
          
def texto_tela(sentimento_positivo, sentimento_negativo, sentimento_neutro, string_resposta_ia):
    print(f"Avaliações negativas: {sentimento_negativo}, Avaliações neutras: {sentimento_neutro}, Avaliações positivas: {sentimento_positivo}\n {string_resposta_ia}");

contar_sentimentos(resposta_ia);
texto_tela(*contar_sentimentos(resposta_ia), string_resposta_ia);