#1Új név rögzítése
#2nevek listázása
#3Kilépés

#Add meg a neved
#Listázza ki a neveket

menutext = """"Válassz az alábbi menüpontok közül!
1 Új Név rögzítése
2 Felvett nevek listázása
3 Kilépés 
"""
#ezzel is működik.
#"Válassz az alábbi menüpontok közül!\n 1 Új Név rögzítése\n 2 Felvett nevek listázása\n 3 Kilépés"

menu = 0
menu_input1 = 1
menu_input2 = 2
menu_exit = 3
nevek = []

while menu != menu_exit:
    print(menutext)
    menu = int(input())
    if menu == menu_input1:
          print("Add meg a neved\n")
          nevek.append(input())
    elif menu == menu_input2:
          print("A felvett nevek listája:" , nevek)
    elif menu == menu_exit:
        print("Viszlát!")
    else:
        print("ismeretlen menüpont")
