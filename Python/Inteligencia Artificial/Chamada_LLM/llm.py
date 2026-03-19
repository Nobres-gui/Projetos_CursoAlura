from openai import OpenAI;

client = OpenAI(
    base_url="http://127.0.0.1:65000/v1",
    api_key="lm-studio"
);

response = client.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[
        {"role": "system", "content": "Você é um assistente de IA que sempre responde apenas a palavra SIM."},
        {"role": "user", "content": "Explique a teoria da relatividade de forma simples."}
    ],
    temperature=1,
    max_tokens=500
);

print(response.choices[0].message.content);
