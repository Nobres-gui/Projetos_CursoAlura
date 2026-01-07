import json;
import requests;

url ="https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json";

response = requests.get(url);
if response.status_code == 200: 
    dados_json = response.json();
    print(f"Arquivo emcontrado com sucesso!!! <{response.status_code}>");
    dados_restaurante = {};
    for item in dados_json:
        nome_restaurante = item["Company"];
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = [];
            
        dados_restaurante[nome_restaurante].append({
            "item": item["Item"],
            "prece": item["price"],
            "description": item["description"]
        });
    
else:
    print(f"O erro foi {response.status_code}");
    
    
for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f"{nome_restaurante}.json";
    with open(nome_arquivo, "w") as file:
        json.dump(dados, file, indent = 4)
        