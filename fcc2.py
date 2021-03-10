import math

def add_time(start, duration, day = None):
    daysOfWeek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if day != None:
        day = day.lower().capitalize()
    start = start.split(':')
    start.append(start[1].split(' '))
    start[0] = int(start[0])
    start[1] = int(start[2][0])
    start[2] = start[2][1]
    duration = duration.split(':')
    days = math.floor(int(duration[0])/24)
    duration[0] = int(duration[0])%24
    duration[1] = int(duration[1])
    start[0] += duration[0]
    start[1] += duration[1]
    if start[1] >= 60:
        start[1] -= 60
        start[0] += 1
    if start[0] > 12:
        start[0] -= 12
        if start[2] == 'PM':
            days += 1
            start[2] = 'AM'
        else:
            start[2] = 'PM'
    elif start[0] == 12:
        if start[2] == 'PM':
            start[2] = 'AM'
            days += 1
        else:
            start[2] = 'PM'
    if start[1] < 10:
        start[1] = '0' + str(start[1])
    res = ''
    if day != None:
        day = daysOfWeek[(daysOfWeek.index(day) + days) % 7]
        res += str(start[0]) + ':' + str(start[1]) + ' ' + str(start[2]) + ', ' + day
    else:
        res += str(start[0]) + ':' + str(start[1]) + ' ' + start[2]
    if days == 1:
        res += ' (next day)'
    elif days > 1:
        res += ' (' + str(days) + ' days later)'
    return res
#-----------------------------------------------------------
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))