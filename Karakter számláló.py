a = "Fekete"

for c in a:
    if c == "e":
        print("van benne e")
        break
    elif c == "E":
        print("van benne E")
        break
    else:
        print ("Nincs benne e")
        break

a = "Fekete"


#Vagy

for c in a:
    if (c == "e") or (c == "E"):
        print("van benne e")
        break