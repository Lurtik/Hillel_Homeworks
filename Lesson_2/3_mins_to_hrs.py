mins = int(input('Введіть кількість хвилин: '))

hours = mins // 60
minutes_left = mins % 60

if 11 <= hours % 100 <= 14:
    hrs = 'годин'
elif hours % 10 == 1:
    hrs = 'година'
elif 2 <= hours % 10 <= 4:
    hrs = 'години'
else:
    hrs = 'годин'

if 11 <= minutes_left % 100 <= 14:
    minutes = 'хвилин'
elif minutes_left % 10 == 1:
    minutes = 'хвилина'
elif 2 <= minutes_left % 10 <= 4:
    minutes = 'хвилини'
else:
    minutes = 'хвилин'

print(hours, hrs, minutes_left, minutes)