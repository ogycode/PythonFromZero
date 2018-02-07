print("Dictionary, (c) Verloka Vadim 2018\n\n\n")



a = {}              #empty
b = {"key1":1, "key2":2, "key3":3}

print("Empty dict: {}".format(a))
print("Simple dict: {}".format(b))

c = dict([(1,1),(2,2),(3,3)])

print("Dict created by dict: {}".format(c))

d = dict.fromkeys(["a", "b", "c", "d"])                 #keys without value
e = dict.fromkeys(["a", "b", "c", "d"], 255)            #keys with some value

print("Dict form fromkeys #1: {}".format(d))
print("Dict form fromkeys #2: {}".format(e))

print("For:")

for i in e:
    print("Key: {0}, Value: {1}".format(i, e.get(i)))