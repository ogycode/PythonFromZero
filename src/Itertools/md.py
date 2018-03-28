print("Itertools, (c) Verloka Vadim 2018\n\n\n")

import itertools

#count = бесконечная последовательность с указываемым началом и шагом
print("count:")
for i in itertools.count(10, 10):
    if i > 1000:
        break
    else:
        print(i, end=' ')

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c = 0

#cycle - бесконечно возвращает по одному элементу из списка
#если список закончился - перечисление начинается с начала
print("\ncycle:")
for i in itertools.cycle(l):
    c += 1
    print(i, end=' ')
    if c > 25:
        break

#повторяет указаный обьект указаное число рас
print("\nrepeat:")
for i in itertools.repeat('A', 13):
    print(i, end=' ')

#сумирует элемент с предыдущим
print("\naccumulate:")
for i in itertools.accumulate(l):
    print(i, end=' ')

#возвращает всевозможные комбинации
# ABC -> AB AC AD BC BD CD
print("\ncombinations:")
for i in itertools.combinations("VERLOKA", 2):
    print("{}{}".format(i[0],i[1]), end=' ')

#тоже самое, что и предыдущее но также искользуются и повторяющиеся элементы
# AB -> AA AB BB BA
print("\ncombinations_with_replacement:")
for i in itertools.combinations_with_replacement("VERLOKA", 2):
    print("{}{}".format(i[0],i[1]), end=' ')

#возвращает элементы для которых предикат
#в данном случае лямбда выражение вернет False
print("\ndropwhile:")
for i in itertools.dropwhile(lambda x: x < 5, l):
    print(i, end=' ')

#тоже, что и предыдущий
print("\nfilterfalse:")
for i in itertools.filterfalse(lambda x: x < 5, l):
    print(i, end=' ')

#возвращает элементы для которых предикат вернут True
print("\ntakewhile:")
for i in itertools.takewhile(lambda x: x < 5, l):
    print(i, end=' ')
