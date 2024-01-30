import requests

URL = 'localhost:5000'


def score_post(score):
    r = requests.post(URL + '/score', data=str(score), timeout=2.50)
    print(r)


def scoreboard():
    r = requests.get(URL + '/scoreboard', timeout=2.50)
    print(r)