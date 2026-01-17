import openai

def classify_and_generate_response(text):
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Classifique este email e sugira uma resposta:\n{text}"}
            ]
        )
        categoria = "Produtivo"
        resposta = response['choices'][0]['message']['content']
        return categoria, resposta

    except openai.error.OpenAIError as e:
        if any(word in text.lower() for word in ["pedido", "solicitação", "ajuda", "dúvida"]):
            categoria = "Produtivo"
            resposta = "Obrigado pelo seu contato. Iremos verificar e responder em breve."
        else:
            categoria = "Improdutivo"
            resposta = "Agradecemos a sua mensagem."

        print(f"[Fallback] OpenAIError: {str(e)}")
        return categoria, resposta
