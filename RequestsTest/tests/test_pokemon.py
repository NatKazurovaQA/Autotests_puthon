import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2/'
TOKEN = '3283383d7477cae36c6c60971c1517ac'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '2475'

def test_trainer_name():
    response_trainer = requests.get(url = f'{URL}trainers', params = {'trainer_id': TRAINER_ID})
    assert response_trainer.json()["data"][0]["id"] == TRAINER_ID

def test_status_code():
    response = requests.get(url = f'{URL}trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200
