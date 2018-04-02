#print("Argparse, (c) Verloka Vadim 2018\n\n\n")

import argparse

def fibonacci(number):
    """Числа фибоначи"""
    a, b = 0, 1

    for i in range(number):
        a, b = b, a + b
    
    return a

def secondDegree(number):
    """Возводит число во вторую степень"""
    return pow(number, 2)

def Main():
    parser = argparse.ArgumentParser()

    parser.add_argument("num", help="Числа Фибоначи", type=int)
    parser.add_argument("-sd", "--secondDegree", help="Вторая степень числа Фибоначи", action="store_true")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s", "--short", help="Компактный вывод", action="store_true")
    group.add_argument("-f", "--full", help="Полный вывод", action="store_true")

    a = parser.parse_args()

    result = fibonacci(a.num)

    if a.full:
        print("The {}th Fibonacci number is {}".format(a.num, result))
    elif a.short:
        print(result)
    else:
        print("fibonacci({}): {}".format(a.num, result))

    if a.secondDegree:
        print("The second degree of result is {}".format(secondDegree(result)))


if __name__ == '__main__':
    Main()

    