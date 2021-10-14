#A felhasználótól kérjünk be 5 számot és válasszuk ki a legnagyobbat
#ird is ki a beírt 5 számot egymás mellé

numbers = []
highest = 0
i = 0

while i <5:
  number = int(input(f"Add meg a {i +1} számot! \n "))
  numbers.append(number)
  i += 1
print(numbers)

result = "Kapott számok: "
i = 0
for number in numbers:
      result = result + str(number) + ", "
      if i != len(numbers) -1:
            result = result + ", "
      i += 1
print(result)

for number in numbers:
    result = result + str(number)
    if i != len(numbers)-1:
        restult = result + ", "
    if number > highest:
        highest-number
print("Ebből a legnagyobb:" highest)

