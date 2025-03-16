import json
import pandas as pd
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import locale

locale.setlocale(locale.LC_ALL, "nb_NO.UTF-8")

tablepos = []
clubs = []
point = []
game = []
goal_diff = []
team_logo = []


def dato():
    now = datetime.now()
    dagens = now.strftime("%A, %d %B %Y, uke %W")
    return dagens


def table():
    with (open('table.json') as f):
        file = f.read()
        data = json.loads(file)
        pl_table = data['response'][0]['league']['standings'][0]
        table_date = dato()
        print(table_date)
        for i in pl_table:
            table_pos = i['rank']
            team = i['team']['name']
            points = i['points']
            games = i['all']['played']
            goals = i['goalsDiff']
            logo = i['team']['logo']
            tablepos.append(table_pos)
            clubs.append(team)
            point.append(points)
            game.append(games)
            goal_diff.append(goals)
            team_logo.append(logo)

        clm = ['Pos', 'Team', 'Games', 'Goals', 'Points', ]
        club_with_logo = [f'<img src="{logo}" alt="Logo" width="20" height="20"> {club}' for logo, club in
                          zip(team_logo, clubs)]
        df = pd.DataFrame(list(zip(tablepos, club_with_logo, game, goal_diff, point)), columns=clm)
        html_table = df.to_html(index=False, escape=False)
        env = Environment(loader=FileSystemLoader('..'))
        template = env.get_template(r'pl-table/template.html')
        output = template.render(table=html_table)
        with open("index.html", "w") as file:
            file.write(output)
        print(df)


if __name__ == '__main__':
    # match_result()
    table()
