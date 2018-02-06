print("Hello World, (c) Verloka Vadim 2018\n\n\n")
name = input("What is your name? ")
print("Nice to meet you,",name)
age = int(input("How old are you? "))
if(age < 20):
    print("So yong...")
    print("I'm 22 years old")
elif 20 <= age <= 30:
    print("Wow, almost age with me...")
    print("I'm 22 years old")
else:
    print("To old...")

print("Testing If-Else:")
print("if 15 < 20 and 15 > 10")

if 15 < 20 and 15 > 10:
    print(True)

print("if not False")

if not False:
    print(True)

print("if 1 > 0 or 5 < 1")

if 1 > 0 or 5 < 1:
    print(True)

print("While testing:")

i = 0
i1 = int(input("Enter number for While: "))

while i < i1:
    i = i + 1
    print("While:",i)

print("For testing #1:")

string = input("Enter string for For: ")

for j in string:
    print(j)

print("For testing #2:")

string = input("Enter string for For: ")

for k in string:
    print("_" + k + "_", end='')            #end='' disable new line















