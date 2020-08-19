import requests
import json
import pprint

#### Bearer Token de acesso
client_access_token = 'AKqLwbINrDB5ArARDt-d7mHESoQEzkZSOoSWXUcAdI5ZvsjneeKJdFsQZCsrqWvg'
#### URL da API
base_url = 'https://api.genius.com'

path = 'search/'
# songs = '/songs'
#### Troca espaços do input por traço
user_input = input('artist: ').replace(" ", "-")

#### Concatena baseURL com path
request_uri = '/'.join([base_url, path])
print(request_uri + user_input)
#### Parametros da busca por input do usuario
params = {'q': user_input,
          'sort': "popularity",
          'per_page': "10",
          'text_format': "plain"}
#### Formata token para requisição
token = 'Bearer {}'.format(client_access_token)
headers = {'Authorization': token}
#### Tras resultado da requisição GET para variavel r
r = requests.get(request_uri, params=params, headers=headers)
#### Converte retorno em texto
data = r.text
#### Converte texto em json
json_data = json.loads(data)
print('Artista: ' + user_input)
#### Cria contador x
x = 0
#### Enquanto x for menor que 10 tras dos hits o nome da musica pela ordem do contador
while (x < 10):
    for hits in json_data["response"]["hits"]:
        x += 1
        print('Top',x, hits["result"]["title"])
