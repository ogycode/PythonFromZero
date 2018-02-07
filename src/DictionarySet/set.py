print("Set, (c) Verloka Vadim 2018\n\n\n")


a = set()           #empty set
c = {}              
e = {"t","t","h","1","v"}
b = set("hello world!")

print("Set: {}".format(b))
print("Set: {}".format(e))

print("h in b: {}".format("h" in b))
print("x in b: {}".format("x" in b))

f = frozenset(b)                        #fromzen set cn not be edited

print("Frozen set: {}".format(f))

