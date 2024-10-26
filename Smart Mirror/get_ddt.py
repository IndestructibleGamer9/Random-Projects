from datetime import datetime

def ddt():
    now = datetime.now()
    date = now.strftime('%d-%m-%Y')
    time = now.strftime('%I:%M %p')
    day = now.strftime('%A')
    # print(f'date: {date} time: {time} day: {day}')
    dtInfo = {
        'date' : date,
        'time' : time,
        'day' : day
    }
    return dtInfo


time =  ddt()
print(time['time'])

 