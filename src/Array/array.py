print("Array, (c) Verloka Vadim 2018\n\n\n")

String = "string"
Array = list(String)

print("String: " + String)
print("Array: " + str(Array))

print("Generator for list:")

l = [l for l in String]

print("Array: " + str(l))

#Добавить елемент в конец
Array.append(" ")                   
Array.append("2")

print("Array: " + str(Array))

#Добавить список в конец списка
Array.extend(Array)            

print("Array: " + str(Array))

#Едалить первое вхождение элемента
Array.remove("t")    
Array.remove("5")

print("Array: " + str(Array))