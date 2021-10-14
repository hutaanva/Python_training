#Írj egy függvényt ami kiírja ,hogy  Hello Functions
#Írj egy függvényt ami két paramétert kap és összeadja ezeket
#Írj egy függvényt ami visszaadja, hogy a paraméterként átadott szöveg hány space karaktert tartalmaz
#Írj egy függvényt ami paraméterként átadott lista átlagát adja vissza
#Írj egy függvényt ami visszaadja, hogy hány magánhangzó van a paraméterként átadott szövegben

def print_hello():
    print("Hello Functions!")

def numbers(érték1,érték2):
    return ertek1+ertek2

def count_spaces():
    print("Hány karakterből áll ez a szöveg vajon?")
    count = 0
    for c in s:
        if c == " ":
            count += 1

def calc_avrg(numbers):
    result = 0
    for number in numbers:
        result += number
    return result / len(numbers)

def count_vowels(s):
    count = 0
    for c in s:
        if c in "aAeEiIoOuU":
            count += 1
    return count

#1
print_hello()

#2
#print(numbers(2,4))
result = numbers(2,4)


