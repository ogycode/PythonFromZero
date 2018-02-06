print("Array, (c) Verloka Vadim 2018\n\n\n")

String = "string"
Array = list(String)

print("String: " + String)
print("Array: " + str(Array))

print("Generator for list:")

l = [l for l in String]

print("Array: " + str(l))

Array.append(" ")                   #add element to and of list
Array.append("2")

print("Array: " + str(Array))

Array.extend(Array)                 #add list to end of list

print("Array: " + str(Array))

Array.remove("t")                   #remove first entering of element
Array.remove("5")

print("Array: " + str(Array))