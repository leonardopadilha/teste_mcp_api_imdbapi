import os
import requests
from fastmcp import FastMCP

servidor_mcp = FastMCP('mcp-imdbapi')

BASE_URL = "https://api.imdbapi.dev"

@servidor_mcp.tool()
def search_title(title: str) -> dict: 
  url = f"{BASE_URL}/search/titles"
  params = {
    "query": title,
    "limit": 1
  }

  response = requests.get(url, params=params)

  try:
    response.raise_for_status()
    resultado = response.json()

  except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    response = None
  else:
    info_imdb = {
      'id': resultado['titles'][0]['id'],
      'tipo': resultado['titles'][0]['type'],
      'titulo': resultado['titles'][0]['originalTitle'],
      'ano_inicio': resultado['titles'][0]['startYear'],
      'pontuacao': resultado['titles'][0]['rating']['aggregateRating']
    }
  
  return info_imdb

@servidor_mcp.tool()
def details_title(id_title_imdb) -> dict:
  url = f"{BASE_URL}/titles/{id_title_imdb}"
  response = requests.get(url)

  try:
    response.raise_for_status()
    resultado = response.json()

  except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    response = None
  else:
    info_imdb = {
      'plot': resultado['plot'],
    }
  
  return info_imdb
  

if __name__ == "__main__":
  servidor_mcp.run(transport='stdio')
