import ollama

def agente_interativo():
    print("="*60)
    print("AGENTE DE IA - (MISTRAL)")
    print("Instruções: Digite sua pergunta ou 'sair' para encerrar.")
    print("="*60)

    historico = [{'role': 'system', 'content': 'Você é um assistente. Responda de forma clara e objetiva em português.'}]

    while True:
        pergunta = input("Pergunta: ")

        if pergunta.lower() in ("sair"):
            print("Até a proxima!")
            break

        historico.append({'role': 'user', 'content': pergunta})

        try:
            print("Pensando...", end="\r")
            response = ollama.chat(model='mistral', messages=historico) 
            resposta_ia = response['message']['content']
            print(f"IA: {resposta_ia}")
            print ("-"*40)
            historico.append({'role': 'assistant', 'content': resposta_ia})
        except Exception as e:
            print(f"\nErro ao conectar com o Ollama: {e}")
            print("Certifique-se de que o Ollama está aberto e o modelo Mistral foi baixado.")
            break

if __name__ == "__main__":
    agente_interativo()
