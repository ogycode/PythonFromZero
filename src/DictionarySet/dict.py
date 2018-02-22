print("Dictionary, (c) Verloka Vadim 2018\n\n\n")



#Пустой словарь
a = {}  
b = {"key1":1, "key2":2, "key3":3}

print("Empty dict: {}".format(a))
print("Simple dict: {}".format(b))

c = dict([(1,1),(2,2),(3,3)])

print("Dict created by dict: {}".format(c))

#Словарь с ключами без значений
d = dict.fromkeys(["a", "b", "c", "d"])

#Словарь с ключами которым присвоено какоето одно значение
e = dict.fromkeys(["a", "b", "c", "d"], 255)

print("Dict form fromkeys #1: {}".format(d))
print("Dict form fromkeys #2: {}".format(e))

print("For:")

for i in e:
    print("Key: {0}, Value: {1}".format(i, e.get(i)))