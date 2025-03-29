import json
import pandas as pd
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


def match_time_stamp(timestamp):
    match_tid = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y")
    return match_tid


def determine_result(homescore, awayscore, home_id, united_id):
    if homescore > awayscore:
        if home_id == united_id:
            return 'Seier'
        else:
            return 'Tap'
    elif homescore < awayscore:
        if home_id == united_id:
            return 'Tap'
        else:
            return 'Seier'
    else:
        return 'Uavgjort'


def format_result_cell(result):
    if result == 'Seier':
        return f'<td class="seier"></td>'
    elif result == 'Uavgjort':
        return f'<td class="uavgjort"></td>'
    elif result == 'Tap':
        return f'<td class="tap"></td>'
    else:
        return f'<td></td>'


def match_result():
    match_time = []
    home_team = []
    away_team = []
    home_score = []
    away_score = []
    result = []

    with (open('../matches/match.json') as f):
        file = f.read()
        data = json.loads(file)
        pl_league = data['response']
        for i in range(len(pl_league)):
            matchtime = pl_league[i]['fixture']['timestamp']
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
                match_time.append(match_time_stamp(matchtime))
                result.append(determine_result(homescore, awayscore, home_id, united_id))
        remove_column_name = ''

        clm = ['Match date', 'Home', 'Away', 'h_score', 'a_score', remove_column_name]
        h_score = [int(score) if score is not None else 0 for score in home_score]
        a_score = [int(score) if score is not None else 0 for score in away_score]

        df = pd.DataFrame(list(zip(match_time, home_team, away_team, h_score, a_score, result)), columns=clm)
        df['Match date'] = pd.to_datetime(df['Match date'], format="%d/%m/%Y")
        df = df.sort_values(by='Match date', ascending=False)
        print(df)
        html_table = df.to_html(index=False, escape=False, classes='dataframe',
                                formatters={remove_column_name: format_result_cell})
        env = Environment(loader=FileSystemLoader('..'))
        template = env.get_template(r'unitedmatches/template.html')
        output = template.render(table=html_table)
        with open("index.html", "w") as file:
            file.write(output)


united_id = 33

if __name__ == '__main__':
    match_result()
