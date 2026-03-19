from google import genai;
from dotenv import load_dotenv;
import os;

load_dotenv();

api_key = os.environ.get("GOOGLE_API_KEY");

if api_key is None:
    print("Erro: A chave não foi encontrada no .env ou nas variáveis de ambiente.")
else:
    # Use sua chave aqui
    print(f"Chave carregada com sucesso")

opcao_usuario = 1;
pergunta_usuario = "";

while opcao_usuario != 2:
    opcao_usuario = int(input(" Escolha as opções a seguir:\n (1)Falar com o chatbot\n (2)Sair \n\n Opção: "));
    
    if opcao_usuario == 2:
        print(" Saindo da aplicação");
        break;
    else:
        while pergunta_usuario != "sair":
            client = genai.Client(api_key = api_key);
            chat = client.chats.create(model="gemini-2.5-flash");
            
            print("\n ***** Para parar a aplicação digite 'sair' *****\n");
            
            pergunta_usuario = input(" Digite sua pergunta: ").lower();
            
            if pergunta_usuario != "sair":
                response = chat.send_message(pergunta_usuario);
                print(f"\n {response.text}");
            else:
                print(" Saindo da aplicação");
                opcao_usuario = 2;

    