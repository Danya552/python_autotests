import requests 
import json

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '37b14e3005bd6bb0b550eb83d03d5f9d'
HEADER = {'Content-type': 'application/json', 'trainer_token':TOKEN}

BODY_create_pok = {
    "name": "Бульбазавр",
    "photo_id": 12
}


'''Создаем покемона'''
response_create_pok = requests.post(url = f'{URL}/pokemons',headers= HEADER, json= BODY_create_pok)

print(response_create_pok.json()['message']) 

pokemon_id =  response_create_pok.json()['id']
print('id Покемона- ', pokemon_id)

'''Меняем имя покемона'''
'''name_pok= input('Введите новое имя Покемона ')'''
BODY_name_pok= {
    "pokemon_id": pokemon_id,
    "name": "Краказябра",
    "photo_id": 2
}

response_change_name = requests.put(url = f'{URL}/pokemons',headers= HEADER, json= BODY_name_pok)
print(response_change_name.json()['message'])

'''Ловим покемона в покеболл'''
BODY_wast_pok = {
    "pokemon_id": pokemon_id
}
response_wast_pok = requests.post(url = f'{URL}/trainers/add_pokeball',headers= HEADER, json= BODY_wast_pok)
print(response_wast_pok.json()['message'])
