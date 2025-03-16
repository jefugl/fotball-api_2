import json
import pandas as pd
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


def match_time_stamp(timestamp):
    match_tid = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y Kl:%H:%M")
    return match_tid


def match_result():
    with (open('../matches/match.json') as f):
        file = f.read()
        data = json.loads(file)
        pl_league = data['response']
        for i in range(len(pl_league)):
            mtime = pl_league[i]['fixture']['timestamp']
            home_id = pl_league[i]['teams']['home']['id']
            away_id = pl_league[i]['teams']['away']['id']
            homescore = pl_league[i]['goals']['home']
            awayscore = pl_league[i]['goals']['away']
            if home_id == united_id or away_id == united_id:
                if homescore is None or awayscore is None:
                    continue
                home_team.append(pl_league[i]['teams']['home']['name'])
                away_team.append(pl_league[i]['teams']['away']['name'])
                home_score.append(pl_league[i]['goals']['home'])
                away_score.append(pl_league[i]['goals']['away'])
                match_time.append(match_time_stamp(mtime))

        clm = ['Match date', 'Home', 'Away', 'h_score', 'a_score']
        h_score = [int(score) if score is not None else 0 for score in home_score]
        a_score = [int(score) if score is not None else 0 for score in away_score]

        df = pd.DataFrame(list(zip(match_time, home_team, away_team, h_score, a_score)),
                          columns=clm)
        print(df)
        print(match_time)
        html_table = df.to_html(index=False, escape=False)
        env = Environment(loader=FileSystemLoader('..'))
        template = env.get_template('unitedmatches/template.html')
        output = template.render(table=html_table)
        with open("index.html", "w") as file:
            file.write(output)


match_time = []
home_team = []
away_team = []
home_score = []
away_score = []

united_id = 33


if __name__ == '__main__':
    match_result()
