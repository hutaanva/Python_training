from bs4 import BeautifulSoup
from requests import get

content = get("https://www.index.hu").text
soup = BeautifulSoup(content, features="html.parser")
only_text= soup.get_text()
lines = only_text.splitlines()
for line in lines:
    if len(line.strip()) != 0:
         print(line)
