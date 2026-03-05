Agente de IA com Mistral e Ollama

Este projeto consiste em um Agente de Inteligência Artificial interativo via terminal. O agente utiliza o modelo de linguagem **Mistral** rodando localmente através do **Ollama**.

#Funcionalidades
- Interface interativa via linha de comando (CLI).
- Memória de curto prazo (mantém o contexto da conversa).
- Especializado em assistência técnica e programação Python.

#Tecnologias Utilizadas
- **Python 3.14** (Compatibilizado com bibliotecas leves).
- **Ollama**: Para orquestração do modelo local.
- **Mistral LLM**: O "cérebro" do agente.
- **Biblioteca Ollama-Python**: Para comunicação entre o código e a IA.

#Como Executar
1. Instale o [Ollama](https://ollama.com/ ).
2. No terminal, baixe o modelo: `ollama pull mistral`.
3. Clone este repositório.
4. Crie um ambiente virtual: `python -m venv .venv`.
5. Ative o ambiente e instale as dependências:
   ```bash
   pip install ollama
