import requests
import json
import pandas as pd

def requests_cep():
    while True:
        try:
            cep = str(input('Digite um CEP:'))
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            data = response.json()
            return data
        except (requests.RequestException,json.JSONDecodeError,KeyError):
            print('Cep Invalido. Tente novamente.')
            continue

data = requests_cep()
for key,value in data.items():
    if not value.strip():
        continue
    print(key + ': ' + value)
    
