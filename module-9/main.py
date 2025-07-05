import requests
import json

response = requests.get(f'https://pokeapi.co/api/v2/pokemon')

print(f'Connection Status: {response.status_code}')

print(f'\nNon-Formatted Output\n\t{response.json()}')

def format(data):
    text = json.dumps(data, sort_keys=True, indent=4)
    return text

print(f'\nFormatted Output\n\t{format(response.json())}')