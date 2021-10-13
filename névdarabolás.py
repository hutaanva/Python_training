i=0
name = "Varga Tamás"
print(len(name))


while i < len(name):
    print(name[i])
    i = i+1


for c in name:
    print(c)


name = "John Doe"
age = 35

#A john Doe alkalmazott 35 éves!

print("A" , name , "alkalmazott ", age, "éves!")

print(f"A {name} alkalmazott {age} éves!")   #f format után meg lehet adni a változókat {} közé

name = "Jack Doe"
print(name[1:6])
print(name[1:6:2])
print(name[::-1])
print(name[:6])

