# Вариант a)
duration = int(input('Введите количество секунд: '))
s = str(duration)
print(s + ' сек ')

# Вариант b)
duration = int(input('Введите количество секунд: '))
m = str((duration //60) % 60)
s = str(duration % 60)
print(m + ' мин ' + s + ' сек ')


# Вариант c)
duration = int(input('Введите количество секунд: '))
h = str(duration // 3600)
m = str((duration //60) % 60)
s = str(duration % 60)
print(h + ' час ' + m + ' мин ' + s + ' сек ')


# Вариант d*)
duration = int(input('Введите количество секунд: '))
d = str(duration // 86400)
h = str((duration // 3600) % 24)
m = str((duration //60) % 60)
s = str(duration % 60)
print(d + ' дн ' + h  + ' час ' + m + ' мин ' + s + ' сек ')