names = ["John Doe", "Jack Doe", "Jane Doe"]
print(len(names))
print(names[1])
#szeletelés
print(names[::-1])

#listába karakterenként veszi fel az elemeket
fruits = ["orange"]
fruits += "apple"
print(fruits)

#listába elemet felvenni
fruits = ["orange"]
fruits.append("apple")
fruits.append("grape")
fruits.append("lemon")
print(fruits)

#ha meg akarod adni hanyadik indexre menjen
fruits.insert(0, "tégla")
print(fruits)

l = ["aaa", "bbb"]
l += ["ccc"]
print(l)

empty = []
print(empty)
empty += ["aaaa"]
print(empty)


#Módosítható lista

numbers = ["x" , "y", "z", "z", "z"]
numbers[1] = "a"
print(numbers)

#A 0-adik elemet törli, aztán meg csak 1 db z-z a listából
del(numbers[0])
print(numbers)
numbers.remove("z")
print(numbers)

print("x" in numbers)
print("z" in numbers)
print("o" in "John Doe")

while "z" in numbers:
    numbers.remove("z")
print(numbers)

#string nem módosítható, így hiba üzenetet fog adni ha karakert akarunk cserélni benne
#name = "john"
#name[1] = "x"
#print(name)

