import requests

def localizar_endereço(cep):
  url = f"https://viacep.com.br/ws/{cep}/json/"
  try:
    resposta = requests.get(url)
    dados = resposta.json()
    if "erro" in dados:
      return None
    else:
      return dados
  except requests.exceptions.RequestException as e:
    return None
  
def listar_estados():
  url=f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/"
  try:
    resposta = requests.get(url)
    dados = resposta.json()
    if "erro" in dados:
      return None
    else:
      estados = []
      for estado in dados:
        estados.append(estado["sigla"])
      return estados
  except requests.exceptions.RequestException as e:
    return None

def municipios_por_estado(estado):
  url=f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/municipios"
  try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
      municipios = []
      for municipio in resposta.json():
        municipios.append(municipio["nome"])
      return municipios
    return None
  except requests.exceptions.RequestException as e:
    return None