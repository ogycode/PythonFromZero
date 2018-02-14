print("Documentation, (c) Verloka Vadim 2018\n\n\n")

def test1():
    """simple empty test function"""
    print("test1()")


def test2(a, b):
    """simple function: print a + b"""
    print("{} + {} = {}".format(a,b,a+b))


def test3():
    """
    multiline\n
    documentation for\n
    simple function
    """
    print("test3()")


test1()
test2(5,22)
test3()