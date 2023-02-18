from datetime import datetime, date
import time


def what_day_is_it(date):

    days = ['1', '2', '3', '4', '5', '6', '7']
    day = date.weekday()

    if days[day] == '7':
        with open('./sunday.html', 'w') as f:
            time.sleep(0.5)
            f.write('<h4>일요일 휴무</h4>')
            time.sleep(0.5)
        f.close()

    if days[day] == '1':
        with open('./sunday.html', 'w') as f:
            time.sleep(0.5)
            f.write('')
            time.sleep(0.5)
        f.close()


what_day_is_it(date.today())
