import json
import requests 
import unicodedata

class Musicas:

    def process(nome):

        client_access_token = 'AKqLwbINrDB5ArARDt-d7mHESoQEzkZSOoSWXUcAdI5ZvsjneeKJdFsQZCsrqWvg'
        base_url = 'https://api.genius.com/search/'
        nome = nome.replace(" ", "-")

        params = {'q': nome,
                  'sort': "popularity",
                  'per_page': "10",
                  'text_format': "plain"}

        token = 'Bearer {}'.format(client_access_token)
        headers = {'Authorization': token}
        r = requests.get(base_url, params=params, headers=headers)
        data = r.text

        json_data = json.loads(data)
        x = 0
        nome = nome.upper()
        saida = (f'Artista : {nome}')
        while (x < 10):
            teste = []
            teste.append(saida)
            for hits in json_data["response"]["hits"]:
                x += 1
                teste2 = {}
                teste2['Top'] = x
                teste2['Musica'] = hits["result"]["title"]
                teste.append(teste2)

        return teste


