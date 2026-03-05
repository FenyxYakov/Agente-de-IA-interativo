import ollama

def agente_interativo():
    print("="*40)
    print("AGENTE DE IA - (MISTRAL)")
    print("Instruções: Digite sua pergunta ou 'sair' para encerrar.")
    print("="*40)

    historico = [{'role': 'system', 'content': 'Você é um assistente. Responda de forma clara e objetiva em português.'}]

    while True:
        pergunta = input("\n Você: ")

        if pergunta.lower() in ['sair', 'exit', 'quit']:
            print("IA: Até a proxima!.")
            break

        historico.append({'role': 'user', 'content': pergunta})

        try:
            print("Pensando...", end="\r")
            response = ollama.chat(model='mistral', messages=historico) 
            resposta_ia = response['message']['content']
            print(f"IA: {resposta_ia}")
            historico.append({'role': 'assistant', 'content': resposta_ia})
        except Exception as e:
            print(f"Erro ao conectar com o Ollama: {e}")
            print("Certifique-se de que o Ollama está aberto e o modelo Mistral foi baixado.")
            break

if __name__ == "__main__":
    agente_interativo()



