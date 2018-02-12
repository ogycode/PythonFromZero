print("Content manager, (c) Verloka Vadim 2018\n\n\n")

#line using in c#

print("Start")

with open("text.txt", "w", encoding="utf-8") as f:
    num = 5
    f.write("1 / {0} = {1}".format(num, 1 / num))
    print("1 / {0} = {1}, was writed to file".format(num, 1 / num))

print("End")
    