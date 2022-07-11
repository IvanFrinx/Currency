import request
import rate
import sys
import my_time
from termcolor import colored
import SQLcommands


if __name__ == '__main__':
    try:
        list_curr = request.currencies()
        connection, cursor = SQLcommands.connect_to_db()
    except Exception as e:
        print(e)
        sys.exit(1)
    SQLcommands.create_table(cursor)
    print("Welcome to currency exchange rate API!\n")
    while True:
        inp = input('Enter command: ').upper().split()

        if len(inp) == 1 and inp[0] == 'QUIT':
            SQLcommands.close_connection(connection, cursor)
            break

        elif len(inp) == 1 and inp[0] == 'HISTORY':
            rates = SQLcommands.history(cursor)
            for i in rates:
                print(i[0], i[1], i[2], colored(round(i[3], 2), i[4]))

        elif len(inp) == 2 and (inp[0] and inp[1]) in list_curr:
            rate_today = request.convert(inp)
            rate_yesterday = request.con_yesturday(inp)
            obj = rate.Rate(my_time.now(), inp[0], inp[1], rate_today,
                            request.colour(rate_today, rate_yesterday))
            print(obj.datetime, obj.curr1, obj.curr2,
                  colored(round(obj.rate, 2), obj.colour))
            SQLcommands.parse_data(obj, cursor, connection)

        else:
            print('Wrong input! Try again!')
