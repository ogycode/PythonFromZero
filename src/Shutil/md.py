print("Module shutil, (c) Verloka Vadim 2018\n\n\n")

import shutil

print("shutil.copyfileobj")

big1 = r"C:\Users\verlo\Desktop\test\big.exe"
big2 = r"C:\Users\verlo\Desktop\test\big2.exe"

#Скопировать содержимое одного файла в другой
#1024 - размер буфера копирования, чтобы большой файл не записывался в память еликом
with open(big2, "wb") as to:
    shutil.copyfileobj(open(big1, "rb"), to, 1024)


print("shutil.copyfile")

code = r"C:\Users\verlo\Desktop\test\code.txt"
code2 = r"C:\Users\verlo\Desktop\test\code2.txt"
code3 = r"C:\Users\verlo\Desktop\test\code3.txt"

#Копирует файл без метаданных
#Если есть - перезапишет
#Если нет - создаст
shutil.copyfile(code, code2)
shutil.copyfile(code, code3)

print("shutil.copymode")

per = r"C:\Users\verlo\Desktop\test\per.txt"

#Копирует права доступа из одного файла в другой
shutil.copymode(per, big1)

print("shutil.chown")

#shutil.copy2 -    Копирует файл в файл или директорию при этом пытается скопировать все метаданные
#shutil.copytree - Копирует дерево директорий
#shutil.rmtree -   Удаляет текущую директорию и все поддиректори
#shutil.move -     Перемещает файл или директорию


print("shutil.disk_usage\nExample1:")

dir = r"C:\Users\verlo\Desktop\test"

#Возвращает статистику использования дискового пространства в байтах
#возвращает кортеж с total, used и free
diskusage = shutil.disk_usage(dir)

print(diskusage)

print("Example2:\nTotal - {} bytes\nUsed - {} bytes\nFree - {} bytes".format(diskusage[0], diskusage[1], diskusage[2]))
print("Example3:\nTotal - {} MB\nUsed - {} MB\nFree - {} MB".format(diskusage[0] / 1024 / 1024, diskusage[1] / 1024 / 1024, diskusage[2] / 1024 / 1024))


print("shutil.get_terminal_size")

#Возвращает размер терминала
print(shutil.get_terminal_size())