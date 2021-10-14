#definiálunk egy függvényt. A defnél felveszi a program az értékeket, de nem történik vele semmi, ahhoz meg kell hívni.

def print_employee():  #függvény deklaráció
    print("John Doe")
    print("developer")
    print("30")

def print_employee_name(employee_name="Anonymous"): #formális paraméter. A paraméternek lehet default értéket adni (employee_name = "Anonymous")
    print("Az alkalmazott neve:" + employee_name)

def print_employee_details(name, position, age):
    print(f"""
          Alkalmazott neve: {name}
          Pozíciója: {position}
          Életkora: {age}
""")

print_employee_name("John Doe")       #függvény hívás: aktuális paraméter
print_employee_name()       #függvény hívás (A deklarálás és a hívás között legyen 2 üres sor): aktuális paraméter

print_employee_details("John Doe", "tester", 30)
print_employee_details("Jack Doe", "DevOps", 25)