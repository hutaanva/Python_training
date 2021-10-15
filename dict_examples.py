products = {"orange": 30, "apple": 50, "bread": 10}

print(products["orange"])
print(products["apple"])

#érték módosítás
products["orange"] = 29
print(products)

#új érték felvétele
products["milk"] = 16
print(products)

my_products = {}
print(my_products)
my_products ["tea"] = 1
print(my_products)

#törlés
del(products["milk"])
print(products)

for key in products.keys():
    print(key + ": " + str(products[key]))

for value in products.values():
    print(value)

if "orange" in products:
    print(" Narancs benne van")

#olyan listát kapsz vissza amiben az értékpárok tople-ek
print(products.items())

for item in products.items():
    print(item[0] + " " + str(item[1]))

for (key,value) in products.items():
    print(key + " " + str(value))

i, j = [1,2]
print(i)
print(j)

