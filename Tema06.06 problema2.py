'''import json
import os


if not os.path.exists("produse.txt"):
    with open("produse.txt", "w") as f:
        f.write("Laptop,5\n")
        f.write("Tableta,30\n")
        f.write("Telefon,8\n")


produse = []

with open("produse.txt", "r") as f:
    for linie in f:
        linie = linie.strip()
        if linie:
            nume, stoc = linie.split(",")
            produse.append({
                "produs": nume.strip(),
                "stoc": int(stoc.strip())
            })


with open("inventar.json", "w") as f_json:
    json.dump(produse, f_json, indent=4)


print("Produse cu stoc mai mic decât 10:")
for p in produse:
    if p["stoc"] < 10:
        print(f"{p['produs']} - Stoc: {p['stoc']}")


nume_nou = input("\nIntroduceți numele noului produs: ")
stoc_nou = int(input("Introduceți stocul: "))

# Adăugăm în listă
produse.append({
    "produs": nume_nou.strip(),
    "stoc": stoc_nou
})


with open("produse.txt", "w") as f:
    for p in produse:
        f.write(f"{p['produs']},{p['stoc']}\n")

with open("inventar.json", "w") as f_json:
    json.dump(produse, f_json, indent=4)

print("\nDupă adăugare, produsele cu stoc mai mic decât 10:")
for p in produse:
    if p["stoc"] < 10:
        print(f"{p['produs']} - Stoc: {p['stoc']}")'''