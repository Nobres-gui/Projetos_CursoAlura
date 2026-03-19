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
        
client = genai.Client(api_key = api_key);

response = client.models.generate_content( model="gemini-2.5-flash", contents="o que é a Ia generativa");

print(response.text);