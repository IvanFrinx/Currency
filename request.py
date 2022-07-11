import requests
import json
import my_time
import os

token = os.getenv('API_TOKEN')


def convert(inp):
    con = requests.get(f"https://free.currconv.com/api/v7/convert?q={inp[0]}_{inp[1]}&compact=ultra&apiKey={token}")
    return float(json.loads(con.content.decode())[f'{inp[0]}_{inp[1]}'])


def con_yesturday(inp):
    con = requests.get(f"https://free.currconv.com/api/v7/convert?q={inp[0]}_{inp[1]}&compact=ultra&date={my_time.yesterday()}&apiKey={token}")
    return float(json.loads(con.content.decode())[f'{inp[0]}_{inp[1]}'][str(my_time.yesterday())])


def currencies():
    con = requests.get(f"https://free.currconv.com/api/v7/currencies?apiKey={token}")
    return json.loads(con.content.decode())['results'].keys()


def colour(rate_today, rate_yesterday):
    if rate_today > rate_yesterday:
        return "green"
    elif rate_today < rate_yesterday:
        return "red"
    else:
        return "white"
