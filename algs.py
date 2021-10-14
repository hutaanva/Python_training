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

nevek = ["Tamás", "Béla", "Tibi", "Gaboto", "Alexandra" "John"]

max = nevek[0]

for nev in nevek:
    if len(nev) > len(max):
                max = nev

print(max)

#számlálás tétele
#Egész szám listából szedjük ki mennyi páros szám van benne

paros = 0

for number in numbers:
    if number % 2 == 0:
        paros = paros+1
print(paros)

#eldöntés tétele
#Nevek között megtalálható e John

for nev in nevek:
    if nev == "John":
        print("Szerepel")
        break
#Szűrés
#Számok listájából válogasd ki egy másik listába a páros számokat

numbers = [10, 2, 3, 1, 4, 5]

even = []   # Üres lista [], üres string "" nem ugyan az

for number in numbers:
    if number % 2 == 0:
       even.append(number)  #változót nem tudod appendelni tehát nem kell a even = even.append(number) csak a vége

print(even)

#Transzformáció (map)
#Hozz létre egy új listát ami a nevek hosszát tartalmazza
#Shift + f6 a változón. Rename variable

nevek = ["Tamás", "Béla", "Tibi", "Gaboto", "Alexandra" "John"]
char = []

for name in nevek:
    char.append(len(name))

print(char)