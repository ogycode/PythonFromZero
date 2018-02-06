print("Strings, (c) Verloka Vadim 2018\n\n\n")

S1 = "Hello, {0}, how are you{1}"

print(S1.format("Vadim", "?"))

print("{:<20}".format("left"))
print("{:>20}".format("right"))
print("{:^20}".format("right"))

print("{:*<20}".format("left"))
print("{:*>20}".format("right"))
print("{:*^20}".format("right"))

print("{:1<20}".format("left"))
print("{:1>20}".format("right"))
print("{:1^20}".format("right"))

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(10076))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(10076))