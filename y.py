import json
import pandas as pd
from datetime import datetime


def match_time_stamp(timestamp):
    match_time = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y Kl:%H:%M")
    return match_time


def match_result():
    with open('matches/match.json') as f:
        file = f.read()
        data = json.loads(file)
        pl_league = data['response']
        length = len(pl_league)
        for i in range(length):
            match_time = pl_league[i]['fixture']['timestamp']
            home_ide = pl_league[i]['teams']['home']['id']
            away_id = pl_league[i]['teams']['away']['id']
            home_team = pl_league[i]['teams']['home']['name']
            away_team = pl_league[i]['teams']['away']['name']
            home_score = pl_league[i]['goals']['home']
            away_score = pl_league[i]['goals']['away']
            home_winner = pl_league[i]['teams']['home']['winner']
            away_winner = pl_league[i]['teams']['away']['winner']
            if home_ide == united_id or away_id == united_id:
                if home_score is None or away_score is None:
                    continue
                print(f'{match_time_stamp(match_time)}: {home_team} {home_score} - {away_team} {away_score}')


a = []
b = []
c = []
d = []
e = []
g = []
h = []
j = []
k = []
l = []
m = []
n = []
o = []
p = []
q = []
r = []
s = []


def table():
    with (open('pl-table/table.json') as f):
        file = f.read()
        data = json.loads(file)
        pl_table = data['response'][0]['league']['standings'][0]
        table_date = pl_table[0]['update']
        print(table_date)
        for i in pl_table:
            table_pos = i['rank']
            a.append(table_pos)
        for i in pl_table:
            team = i['team']['name']
            b.append(team)
        for i in pl_table:
            points = i['points']
            c.append(points)
        for i in pl_table:
            games = i['all']['played']
            d.append(games)
        for i in pl_table:
            win = i['all']['win']
            e.append(win)
        for i in pl_table:
            draw = i['all']['draw']
            g.append(draw)
        for i in pl_table:
            loose = i['all']['lose']
            h.append(loose)
        for i in pl_table:
            goal_for = i['all']['goals']['for']
            j.append(goal_for)
        for i in pl_table:
            goal_against = i['all']['goals']['against']
            k.append(goal_against)
        for i in pl_table:
            games_home = i['home']['played']
            l.append(games_home)
        for i in pl_table:
            games_home_win = i['home']['win']
            m.append(games_home_win)
        for i in pl_table:
            games_home_draw = i['home']['draw']
            n.append(games_home_draw)
        for i in pl_table:
            games_home_loose = i['home']['lose']
            o.append(games_home_loose)
        for i in pl_table:
            games_away = i['away']['played']
            p.append(games_away)
        for i in pl_table:
            games_away_win = i['away']['win']
            q.append(games_away_win)
        for i in pl_table:
            games_away_draw = i['away']['draw']
            r.append(games_away_draw)
        for i in pl_table:
            games_away_loose = i['away']['lose']
            s.append(games_away_loose)

        clm = ['Rank', 'Team', 'Games', 'Points']
        # 'win', 'draw', 'loose', 'goal_for', 'goal_against', 'games_home', 'home_win', 'home_draw', 'home_loose', 'games_away', 'away_win', 'away_draw', '_away_loose'

        df = pd.DataFrame(list(zip(a, b, d, c,)), columns=clm)
        #print(df)
        #df.to_excel(path, index=False, engine='openpyxl')
        # Convert DataFrame to HTML
        html_table = df.to_html(index=False)

        # Save the HTML to a file
        with open("pl-table/table.html", "w") as file:
            file.write(html_table)


path = r"C:\fotball\tabell.xlsx"
united_id = 33

if __name__ == '__main__':
    match_result()
    # table()
