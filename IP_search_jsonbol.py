#írd ki az ip-címeket
#ird ki az ip címek első tagját! xxx.xx.xxx.xx > az első hármast
#ebből a legkisebbet
from json import load

file = open("MOCK_DATA.json", encoding="utf-8")
content = load(file)
min = 255

for item in content:
    ip = item["ip_address"]
    prefix = int(ip.split(".") [0])
    if prefix < min:
        min = prefix
print(min)

#legkisebb első érték keresés.