import requests
import json
import my_time

token = 'c54ef9cbd87f63698820'

def convert(inp):
    con = requests.get(f"https://free.currconv.com/api/v7/convert?q={inp[0]}_{inp[1]}&compact=ultra&apiKey={token}")
    return float(json.loads(con.content.decode())[f'{inp[0]}_{inp[1]}'])

def con_yesturday(inp):
    con = requests.get(f"https://free.currconv.com/api/v7/convert?q={inp[0]}_{inp[1]}&compact=ultra&date={my_time.yesterday()}&apiKey={token}")
    return float(json.loads(con.content.decode())[f'{inp[0]}_{inp[1]}'][str(my_time.yesterday())])

def currencies():
    c = requests.get(f"https://free.currconv.com/api/v7/currencies?apiKey={token}")
    return json.loads(c.content.decode())['results'].keys()

def colour(inp):
    if convert(inp) > con_yesturday(inp):
        return "green"
    elif convert(inp) < con_yesturday(inp): 
        return "red"
    else:
        return "white"     
