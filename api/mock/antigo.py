import requests
import json
import pprint


client_access_token = 'AKqLwbINrDB5ArARDt-d7mHESoQEzkZSOoSWXUcAdI5ZvsjneeKJdFsQZCsrqWvg'
base_url = 'https://api.genius.com'

path = 'search/'
songs = '/songs'
user_input = input('artist: ').replace(" ", "-")


request_uri = '/'.join([base_url, path])
print(request_uri + user_input)

params = {'q': user_input,
          'sort': "popularity",
          'per_page': "10",
          'text_format': "plain"}

token = 'Bearer {}'.format(client_access_token)
headers = {'Authorization': token}

r = requests.get(request_uri, params=params, headers=headers)

data = r.text

json_data = json.loads(data)
print('Artista: ' + user_input)
x = 0
while (x < 10):
    for hits in json_data["response"]["hits"]:
        x += 1
        print('Top',x, hits["result"]["title"])
