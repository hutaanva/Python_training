from datetime import datetime

from requests import get

response= get("https://www.training360.com/")
#print(response.text)
lines = response.text.splitlines() #sorokban adja vissza
print(lines)

#Letölteni az index fő oldalát és megszámolni, hogy hány sorban szerepel a koronavírus szó
#Ezt hozzáfűzi a korona.txt állományba
#írd ki mellé a fileba a dátumot&időt is (google)


response= get("https://index.hu/")
body = response.text
line = body.splitlines()
count = 0
for line in lines:
    if "koronavírus" in line.lower():
        count += 1
now = datetime.now()
with open ("korona.txt", mode="a") as f:
    f.write(f"{now} - {count}\n")

