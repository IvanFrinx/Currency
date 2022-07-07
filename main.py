import request
import rate
import my_time
from termcolor import colored


if __name__ == '__main__':
    objs = list()
    go = True
    try:
        list_curr = request.currencies()
    except:
        go = False
        print("Something's wrong!")
    while go:
        inp = input('Enter command: ').upper().split()

        if len(inp) == 1 and inp[0] == 'QUIT':
            break

        elif len(inp) == 1 and inp[0] == 'HISTORY':
            for obj in objs:
                print(obj.date, obj.curr1, obj.curr2, colored(obj.rate, obj.colour))

        elif len(inp) == 2 and (inp[0] and inp[1]) in list_curr:
            obj = rate.Rate(my_time.now(), inp[0], inp[1], request.convert(inp), request.colour(inp))
            objs.append(obj)
            print(obj.date, obj.curr1, obj.curr2, colored(round(obj.rate, 2), obj.colour))

        else:
            print('Wrong input! Try again!')

