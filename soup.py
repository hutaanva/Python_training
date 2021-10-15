from bs4 import BeautifulSoup
from requests import get

content = get("https://www.index.hu").text
soup = BeautifulSoup(content, features="html.parser")
only_text= soup.get_text()
lines = only_text.splitlines()
counters = {}   #counters legyen dictionary
for line in lines:
    if len(line.strip()) != 0:
         #print(line)
         words = line.split(" ")
         for word in words:
             transformed_word = word.strip().strip(".,:)(").strip(",").lower()
             if len(transformed_word) != 0:
               print(transformed_word)
             if transformed_word not in counters:
                 counters[transformed_word] = 1
             else:
                 counters[transformed_word] += 1
print(counters)

max_word = ""
max_count = 0
for word, counter in counters.items(): #első változó felveszi a kulcsot a második az értékeket és kell a .items() mert nélküle csak a key-eken megy végig nekünk pedig mindenen kell
    if counter > max_count:
        max_word = word
        max_count = counter
print(max_word + " - " + str(max_count))