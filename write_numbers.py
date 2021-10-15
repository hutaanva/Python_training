with open("numbers.txt", encoding="utf-8", mode="a") as f: # "w" a write az "a" az append.
    for i in range(10):
        f.write(f"Szam: {i}\n ")