import requests
import http.client
from key import kee_string


class PremierLeague:
    def __init__(self, url):
        self.url = url

    def pl_api(self):
        payload = {}
        headers = {
            'x-rapidapi-key': kee_string,
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        response = requests.request("GET", self.url, headers=headers, data=payload)
        return response


