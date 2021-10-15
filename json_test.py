from json import load

file = open("characters.json")
content = load(file)

characters = content["characters"]
for character in characters:
    print(character["characterName"])