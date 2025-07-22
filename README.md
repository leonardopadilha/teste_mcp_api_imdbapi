# Projeto API IMDB API

Este projeto utiliza a API IMDB API para buscar informações sobre filmes e séries, combinando com a API do OpenAI para gerar respostas em linguagem natural.

## Configuração

1. **Instalar dependências:**
```bash
pip install fastmcp openai python-dotenv requests
```

2. **Configurar variáveis de ambiente:**
Crie um arquivo `.env` na raiz do projeto com:
```
CHAVE_OPENAI=sua_chave_openai_aqui
```

## Como executar

1. **Iniciar o servidor MCP:**
```bash
python servidor_imdbapi.py
```

2. **Em outro terminal, executar o cliente:**
```bash
python cliente_imdbapi.py
```

## Estrutura do projeto

- `servidor_imdbapi.py`: Servidor MCP que expõe as funções da API IMDB
- `cliente_imdbapi.py`: Cliente que usa o servidor MCP e integra com OpenAI

## Funcionalidades

- Busca de títulos na API IMDB
- Obtenção de detalhes de filmes/séries
- Integração com OpenAI para respostas em linguagem natural
- Avaliação de filmes baseada no rating 


3. **Arquivo JSON para inclusão do MCP:**
```
{
  "mcpServers": {
    "busca-titulos-imdb": {
      "command": "C:\\Caminho\\uv.exe",
      "args": [
        "--directory",
        "D:\\pasta\\local-do-arquivo",
        "run",
        "servidor_imdbapi.py"
      ],
      "description": "Um servidor MCP que faz buscas na API IMDB."
    }
  }
}
```