print("Files, (c) Verloka Vadim 2018\n\n\n")

TextFile = open("text.txt", mode="w")

TextFile.write("Hello!\n")
TextFile.write("World!")

TextFile.close()

TextFile2 = open("text.txt", mode="r")

for i in TextFile2:
    print(i)

TextFile2.close()

# r - read
# w - write (crate or clear)
# x - open for read else exception
# a - append
# b - open like bin
# t - open like text
# + - read/write