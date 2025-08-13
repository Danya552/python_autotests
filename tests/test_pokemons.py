import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '37b14e3005bd6bb0b550eb83d03d5f9d'
HEADER = {'Conten-type': 'application/json', 'trainer_token':TOKEN}
trainer_id = '37858'


def test_status_code():
    response= requests.get(url = f'{URL}/trainers/')
    assert response.status_code == 200

def test_trainer_name():
    response_name= requests.get(url = f'{URL}/trainers/', params= {'trainer_id':trainer_id})
    assert response_name.json()['data'][0]['trainer_name'] == 'ProstDanya'
   