import requests
import http.client
from key import kee_string


def matches():
    url = ' https://v3.football.api-sports.io/fixtures?league=39&season=2024'
    payload = {}
    headers = {
        'x-rapidapi-key': kee_string,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    spamspam = response.text

    with open('matches/match.json', 'w') as f:
        f.write(spamspam)


def standings():
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': kee_string
        }

    conn.request("GET", "/standings?league=39&season=2024", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))
    data_write = data.decode("utf-8")

    with open('pl-table/table.json', 'w') as f:
        f.write(data_write)


if __name__ == '__main__':
    matches()
    standings()
