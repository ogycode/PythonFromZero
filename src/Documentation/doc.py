print("Documentation, (c) Verloka Vadim 2018\n\n\n")

def test1():
    """Описание функции"""
    print("test1()")


def test2(a, b):
    """функция сумирования: print a + b"""
    print("{} + {} = {}".format(a,b,a+b))


def test3():
    """
    многолинейное\n
    описание для\n
    простой функции
    """
    print("test3()")


test1()
test2(5,22)
test3()