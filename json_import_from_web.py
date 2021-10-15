import requests as requests

response = requests.get("https://raw.githubusercontent.com/jeffreylancaster/game-of-thrones/master/data/characters.json")
content = response.json()

characters = content ["characters"]
for character in characters:
    print(character["characterName"])