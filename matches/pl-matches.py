import json
import pandas as pd
from datetime import datetime


def match_time_stamp(timestamp):
    match_tid = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y Kl:%H:%M")
    return match_tid


def match_result():
    with open('match.json') as f:
        file = f.read()
        data = json.loads(file)
        pl_league = data['response']

        for i in range(len(pl_league)):
            match_time.append(match_time_stamp(pl_league[i]['fixture']['timestamp']))
            home_team.append(pl_league[i]['teams']['home']['name'])
            away_team.append(pl_league[i]['teams']['away']['name'])
            h_score.append(pl_league[i]['goals']['home'])
            a_score.append(pl_league[i]['goals']['away'])
            home_winner = pl_league[i]['teams']['home']['winner']
            away_winner = pl_league[i]['teams']['away']['winner']

        clm = ['Match date', 'Home', 'Away', 'h_score', 'a_score']
        home_score = [int(score) if score is not None else 0 for score in h_score]
        away_score = [int(score) if score is not None else 0 for score in a_score]
        df = pd.DataFrame(list(zip(match_time, home_team, away_team, home_score, away_score)), columns=clm)

        html_table = df.to_html(index=False, escape=False)
        with open("matches.html", "w") as file:
            file.write(html_table)


match_time = []
home_team = []
away_team = []
h_score = []
a_score = []

united_id = 33

if __name__ == '__main__':
    match_result()
