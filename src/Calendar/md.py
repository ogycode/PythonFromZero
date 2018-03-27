print("Calendar, (c) Verloka Vadim 2018\n\n\n")

import calendar

c = calendar.Calendar(0)

#возвращает все даты из определенного месяца
print("itermonthdays:")
for f in c.itermonthdays(2018, 8):
    print(f, end=' ')

#возвращает все даты указаного месяца в виде кортежа (дата, номер дня недели)
print("\nitermonthdays2:")
for f in c.itermonthdays2(2018, 8):
    print(f)

#возвращает матрицу содержащую недли с даатами месяца
print("monthdatescalendar:")
for row in c.monthdatescalendar(2018, 3):
    for col in row:
        print(col, end=' ')
    print('\r')

#возвращает первый день недели 0 - понедельник и т.д.
print("firstweekday: {}".format(calendar.firstweekday()))

#является ли год высокосным
print("2018 is leap: {}".format(calendar.isleap(2018)))
print("2019 is leap: {}".format(calendar.isleap(2019)))
print("2020 is leap: {}".format(calendar.isleap(2020)))
print("2021 is leap: {}".format(calendar.isleap(2021)))

#количество высокосных лет в промежутке
print("leap years beetwen 2000 and 2020: {}".format(calendar.leapdays(2000, 2020)))

#номер дня для указаной даты 0 - понедельник и т.д.
print("weekday: {}".format(calendar.weekday(2018, 3, 28)))