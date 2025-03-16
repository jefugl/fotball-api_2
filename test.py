from oob_spam import PremierLeague


def fixture(url):
    pl_fix = PremierLeague(url)
    response = pl_fix.pl_api()
    print(response.text)


def table(url):
    pl_table = PremierLeague(url)
    response = pl_table.pl_api()
    print(response.text)


link = ' https://v3.football.api-sports.io/fixtures?league=39&season=2024'
link2 = 'https://v3.football.api-sports.io/standings?league=39&season=2024'


if __name__ == '__main__':
    fixture(link)
    table(link2)
