import requests
import json

token = 'c54ef9cbd87f63698820'

def convert(inp):
    con = requests.get(f"https://free.currconv.com/api/v7/convert?q={inp[0]}_{inp[1]}&compact=ultra&apiKey={token}")
    return con.content.decode()

def currencies():
    c = requests.get(f"https://free.currconv.com/api/v7/currencies?apiKey={token}")
    return json.loads(c.content.decode())['results'].keys()

def valid_inp():
    return input('Enter command: ').upper().split()  



if __name__ == '__main__':
    go = True
    try:
        list_curr = currencies()
    except:
        go = False
        print("Something is wrong!")
    while go:
        inp = valid_inp()
        if len(inp) == 1 and inp[0] == 'QUIT':
            break
        elif len(inp) == 1 and inp[0] == 'HISTORY':
            print('HISTORY')
        elif len(inp) == 2 and (inp[0] and inp[1]) in list_curr:
            print("Valid curr input")
            con = convert(inp)
            print(con)
        else:
            print('Wrong input! Try again!')

