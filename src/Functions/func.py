print("Functions, (c) Verloka Vadim 2018\n\n\n")

#Простая функция
def Add(x, y):
    return x + y

#Функция с аргументами по умолчанию
def Test1(x,y,z=10,g = 15):
    print("Test1({0},{1},{2},{3}): {0},{1},{2},{3}".format(x,y,z,g))

#Функция с любым количеством аргументов
def Test2(*args):
    for i in args:
        print(i, end=" ")

#Функцяи с любым количеством именованых аргументов
def Test3(**args):
    for i in args:
        print("{0}: {1}".format(i, args[i]), end=" ")


print("Function Add(5,4): {}".format(Add(5,4)))

Test1(10,20)
Test1(10,20,15)
Test1(44,55,g=55)

Test2(5,6,7,8,9)
Test3(a = 11,b = 22,c = 33,d = 44,e = 55,g = 66,z = 77,i = 88,j = 99)


a = lambda x,y: x*y
print("\nlambda function - a(10,25): {}".format(a(10,25)))