#Összegzés tétele
#egészszámokat tartalmazó lista elemeit adjuk össze

numbers = [10, 2, 3, 1, 4, 5]
sum = 0

print(numbers)
for number in numbers:
    sum += number
print(number)

#Szélsőérték keresés tétele

min = numbers[0]
for number in numbers:
    if number < min:
        min = number  #replace-elni a számot a legkisebbel
print(min)

#van egy nevek listája, keresd ki belőle a leghosszabbat

nevek = ["Tamás", "Béla", "Tibi", "Gaboto", "Alexandra"]

max = nevek[0]

for nev in nevek:
    if len(nev) > len(max):
                max = nev

print(max)