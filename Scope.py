def print_info():
    name = "John Doe"
    print("Függvényen belül:" + name)
    return name
def append_chars(name):
    print("tralalala") # a fő programban meghívhatunk egy másik függvényt, ezt nem mi írtuk meg. Ez a hívási lánc. Amikor a függvény önmagát hívja meg az a rekurzió
    return "xxx" + name + "xxx"

### ^fő program

employee = print_info()
print("Függvényen kívül" + employee)

### ˇ Itt meghívom az append_chars és megadjuk neki a John paramétert és kíratjuk a return értéket

employee = append_chars("John")
print(employee)
