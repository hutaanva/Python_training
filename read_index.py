#file nyitás és beolvasás file lezárással együtt. (Mindig le kell zárni a file-t a munka befejeztével.
# #A break parancs is lezárja a file-t.

with open("sample.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip()) #a .strip() kiszedi a space-eket, sörtörést.

# s= f.read()
#    print(s)
#Egyben olvassa be az egészéet és nem soronként mint a for ciklusos

