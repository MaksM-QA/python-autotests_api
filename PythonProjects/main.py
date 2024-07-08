import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '330243ee89d4326f628e2a262d891030'
HEADER ={'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_pokemons = {
    "name": "qwerty",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "42423",
    "name": "qwertymon",
    "photo_id": 2
}

body_addpokeb = {
    "pokemon_id": "42423"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)

pokemon_id = response.json()["id"]
print(pokemon_id)'''

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_addpokeb = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeb)
print(response_addpokeb.text)

