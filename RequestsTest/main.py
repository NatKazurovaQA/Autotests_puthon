import requests

URL = 'https://api.pokemonbattle.me/v2/'
TOKEN = '3283383d7477cae36c6c60971c1517ac'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

Body_pokemons = {
    "name": "Черепашкинс",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response = requests.post(url = f'{URL}pokemons', headers = HEADER, json = Body_pokemons)
print(response.text)

pokemon_id = response.json()['id']

Body_change = { 
    "pokemon_id": pokemon_id, 
    "name": "Черепашкинс2",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
    }

response_change = requests.put(url = f'{URL}pokemons', headers = HEADER, json = Body_change)
print(response_change.text)

Body_poketball = {
    "pokemon_id": pokemon_id
}

response_poketball = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = Body_poketball)
print(response_poketball.text)
