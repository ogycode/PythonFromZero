print("OS.Path, (c) Verloka Vadim 2018\n\n\n")

import os.path

folder = r"C:\Users\verlo\Desktop\test"
folder2 = r"C:\Users\verlo\Desktop\test2"
textFile = r"C:\Users\verlo\Desktop\test\test.txt"
textFile2 = r"C:\Users\verlo\Desktop\test\test2.txt"

#возвращает абсолютный путь
print("abspath: {}".format(os.path.abspath(folder)))

#возвращает базовое имя
print("folder basename: {}".format(os.path.basename(folder)))
print("text file basename: {}".format(os.path.basename(textFile)))

#вовзврщает имя дериктории в которой находится обьект пути (папка/файл)
print("folder dirname: {}".format(os.path.dirname(folder)))
print("text file dirname: {}".format(os.path.dirname(textFile)))

#существует ли дериктория или файл
print("exist? {}: {}".format(folder, os.path.exists(folder)))
print("exist? {}: {}".format(folder2, os.path.exists(folder2)))
print("exist? {}: {}".format(textFile, os.path.exists(textFile)))
print("exist? {}: {}".format(textFile2, os.path.exists(textFile2)))

#возвращает домашний каталог пользователя
#~ - текущий пользователь
#~username - каталог пользоателя username
print("expanduser ~: {}".format(os.path.expanduser("~")))
print("expanduser ~username: {}".format(os.path.expanduser("~username")))

#время последнего доступа к файлу в секундах
print("getatime: {} sec".format(os.path.getatime(textFile)))

#время последнего редактирования файла в секундах
print("getmtime: {} sec".format(os.path.getmtime(textFile)))

#время создания файла в сеундах
print("getсtime: {} sec".format(os.path.getctime(textFile)))

#размер файла в байтах
print("getсtime: {} byte".format(os.path.getsize(textFile)))

#это файл? это директория?
print("isfile {}: {}".format(textFile,os.path.isfile(textFile)))
print("isfile {}: {}".format(folder,os.path.isfile(folder)))
print("isdir {}: {}".format(folder,os.path.isdir(folder)))
print("isdir {}: {}".format(textFile,os.path.isdir(textFile)))





