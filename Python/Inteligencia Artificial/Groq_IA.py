from groq import Groq
from dotenv import load_dotenv;
import os;

load_dotenv();

api_key = os.environ.get("GROQ_API_KEY");

if api_key is None:
    print("Erro: A chave não foi encontrada no .env ou nas variáveis de ambiente.")
else:
    # Use sua chave aqui
    print(f"Chave carregada com sucesso")

client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")