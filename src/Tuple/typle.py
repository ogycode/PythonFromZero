print("Typle, (c) Verloka Vadim 2018\n\n\n")

#Tuple - size less then in array(list)
#Tuple - saving for change (non-edit)
#Tuple - faster then array(list)

array = [1,2,3,4,5]
tupl = (1,2,3,4,5)

print("Array: " + str(array))
print("Typle: " + str(tupl))

print("Array size: " + str(array.__sizeof__()))
print("Typle size: " + str(tupl.__sizeof__()))

emptyTuple = tuple()
emptyTuple2 = ()
tupleFromWord = tuple('tuple')

print("Tuple from word: " + str(tupleFromWord))

#SWAP

a = 15
b = 20

print("A: " + str(a) + "\nB: " + str(b))
print("After swap:")

a,b = b,a

print("A: " + str(a) + "\nB: " + str(b))


