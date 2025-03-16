import requests
import http.client
from key import kee_string


url = 'https://v3.football.api-sports.io/standings?league=39&season=2024'

payload = {}

headers = {
        'x-rapidapi-key': kee_string,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
response = requests.request('GET', url, headers=headers, data=payload)
spam = response.text
print(spam)
