name = "John Doe"
result = ""
counter = 0

for a in name:
    result += a
    if counter < len(name) -1:
           result += ", "
    counter += 1
print(result)

result = name [::-1]
print(result)

result = ""
for a in name:
    result = a + result
print(result)

#palindrom e

print(name == name[::-1])
print(name == result)