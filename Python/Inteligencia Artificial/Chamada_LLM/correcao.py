# contato_com_llm.py
import json
from openai import OpenAI

lista_de_resenhas = []
with open("C:\\Users\\guilh\\Downloads\\Alura\\curso_alura\\Python\\Inteligencia Artificial\\Chamada_LLM\\Desafio_text.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

# print(lista_de_resenhas)

client = OpenAI(
    base_url="http://127.0.0.1:65000/v1",
    api_key="lm-studio"
)

def recebe_linha_e_retorna_json(linha):
    resposta_do_llm = client.responses.create(
        model="google/gemma-3-1b",
        input=[
            {"role": "system", "content": """
            Você é um especialista em análise de dados e conversão de dados para JSON.
            Você receberá uma linha de texto que é uma resenha de um aplicativo em um marketplace online.
            Eu quero que você analise essa resenha, e me retorne um JSON com as seguintes chaves:
            - 'usuario': o nome do usuário que fez a resenha
            - 'resenha_original': a resenha no idioma original que você recebeu
            - 'resenha_pt': a resenha traduzida para o português
            - 'avaliacao': uma avaliação se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra' (apenas uma dessas opções)
            """},
            {"role": "user", "content": f"Resenha: {linha}"}
        ],
        temperature=0.0
    )
    return resposta_do_llm.output_text


lista_de_resenhas_json = []

for resenha in lista_de_resenhas:
    resenha_json = recebe_linha_e_retorna_json(resenha)
    print(resenha_json);
    resenha_dict = json.loads(resenha_json) 
    
    lista_de_resenhas_json.append(resenha_dict)

def contador_e_juntador(lista_de_dicionarios):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0

    for dicionario in lista_de_dicionarios:
        if dicionario['avaliacao'] == 'Positiva':
            contador_positivas += 1
        elif dicionario['avaliacao'] == 'Negativa':
            contador_negativas += 1
        else:
            contador_neutras += 1

    lista_de_dicionarios_str = [str(dicionario) for dicionario in lista_de_dicionarios]
    textos_unidos = "#####".join(lista_de_dicionarios_str)

    return contador_positivas, contador_negativas, contador_neutras, textos_unidos

pos, neg, neut, textos = contador_e_juntador(lista_de_resenhas_json)

print(f"Positivas: {pos}")
print(f"Negativas: {neg}")
print(f"Neutras: {neut}")
print(textos)