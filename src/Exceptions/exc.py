print("Exceptions, (c) Verloka Vadim 2018\n\n\n")

i = 5

try:
    print(i / 0)
except ZeroDivisionError:
    print("Zero Division Error")
finally:
    print("Finally block")

try:
    i = i + "q"
except BaseException:
    print("Base exception")