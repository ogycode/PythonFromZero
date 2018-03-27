print("OS, (c) Verloka Vadim 2018\n\n\n")

import os

print("Name os operation system: {}\n".format(os.name))

#переменные окружения
print("Environment names:\n{")
for i in os.environ:
    print("    {}".format(i))
print("}")

#пример для получения значения переменных среды
#это обычный словарь, переменные можно редактировать/удалять/добавлять
print("Path to Winodws folder: {}".format(os.environ.get("WINDIR")))
print("Path to OneDrive folder: {}".format(os.environ.get("ONEDRIVE")))

print("\nName of current user: {}".format(os.getlogin()))
print("Id of current process: {}".format(os.getpid()))
print("Current work directory: {}".format(os.getcwd()))

print("Files and directories in folder:\n{")
for i in os.listdir("C:\Windows"):
    print("    {}".format(i))
print("}")