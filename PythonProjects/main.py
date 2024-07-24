import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '27a1d76328d93ab0b7c66696edc0021f'
HEADER = {'Content-type': 'application/json', 'trainer_token': TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "lastin200@yandex.ru",
    "password": "apozeb52"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_pokeball = {
    "pokemon_id": "44615"
}

response_registration = requests.post(url = f'{URL}/trainers/reg' , headers = HEADER, json = body_registration)
print (response_registration)


response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email' , headers = HEADER, json = body_confirmation)
print (response_confirmation.text)

response_create = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_create )
print (response_create.status_code)


response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER, json = body_pokeball )
print (response_pokeball.status_code)

pokemon_id = response_create.json()['id']
print(pokemon_id)

