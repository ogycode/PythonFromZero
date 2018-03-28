print("Random, (c) Verloka Vadim 2018\n\n\n")

import random

print("setup rundom seed as 2018")
random.seed(2018)

#каоличество случайных битов
print("getrandbits(17): {}".format(random.getrandbits(17)))

#случайное в промежутке
print("randrange(10,1000,1): {}".format(random.randrange(10,1000,1)))

#случайное целое число
print("randint(10,100): {}".format(random.randint(10,100)))

l = [[1,2],[3,4],[5,6],[7,8],[9,10]]

#случайныъ елемент последовательности
print("choice(l): {}".format(random.choice(l)))

print("before shuffle:")
for i in l:
    print(i, end=' ')

#перемешивает последовательность
random.shuffle(l)

print("\nafter shuffle:")
for i in l:
    print(i, end=' ')

#Случайное число с плавающей точкой в промежутке
print("\nuniform(10,100): {}".format(random.uniform(10,100)))