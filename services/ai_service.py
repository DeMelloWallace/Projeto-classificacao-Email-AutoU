from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def classify_and_generate_response(email_text):
    prompt = f"""
Classifique o email abaixo como Produtivo ou Improdutivo e gere uma resposta educada e profissional.

Email:
{email_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente corporativo especializado em emails."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    output = response.choices[0].message.content

    categoria = "Produtivo" if "Produtivo" in output else "Improdutivo"

    return categoria, output
