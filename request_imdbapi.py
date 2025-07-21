import requests

BASE_URL = "https://api.imdbapi.dev"

def search_title(title): 
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

def details_title(id_title_imdb):
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
  title = input("Digite o título a ser pesquisado: ")
  info_imdb = search_title(title)
  print(info_imdb)

  resumo = details_title(info_imdb['id'])
  print(resumo)
