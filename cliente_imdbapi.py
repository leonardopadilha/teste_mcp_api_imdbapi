import os
import json
import asyncio
from dotenv import load_dotenv
from openai import OpenAI
from fastmcp import Client

load_dotenv()
openai_api_key = os.environ['CHAVE_OPENAI']

caminho_servidor = 'http://localhost:8000/sse'
cliente_mcp = Client(caminho_servidor)

async def search_title_imdbapi(cliente, title):
  async with cliente:
      resultado = await cliente.call_tool('search_title', arguments={"title": title})
      resumo_dict = json.loads(resultado[0].text)
      id_imdbapi_dict = resumo_dict['id']
      resumo = await cliente.call_tool('details_title', arguments={"id_title_imdb": id_imdbapi_dict})
      
      mensagem_sistema = f"""
      Você é um assistente de IA que busca informações sobre filmes e séries na API IMDB API.
      Você deve responder as perguntas do usuário com base nas informações encontradas na API.

      Retorne em português brasileiro as informações encontradas em {resultado[0].text} de forma organizada e legível. 
      Se a pontuação, for maior do que 7, indique esse título de uma maneira criativa.

      O resumo do filme/série deve ser informado conforme retorno da API IMDB API{resumo}, retorne em português brasileiro.
      """

      client = OpenAI(api_key=openai_api_key)
      response = client.responses.create(
        model="gpt-4o-mini",
        instructions=mensagem_sistema,
        input = "Qual o título do filme/série que você deseja buscar?"
      )
      #print(response.output_text)

if __name__ == "__main__":
  title = input("Digite o título do filme/série que você deseja buscar: ")
  asyncio.run(search_title_imdbapi(
    cliente = cliente_mcp,
    title = title
  ))