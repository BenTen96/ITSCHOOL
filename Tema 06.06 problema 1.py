'''import json

print("Introduceți elevii (nume prenume nota), câte unul pe linie.")
print("Când ați terminat, apăsați Enter pe o linie goală.")

elevi_input = []
while True:
    linie = input()
    if linie == "":
        break
    elevi_input.append(linie)

with open("elevi.txt", "w") as f:
    for elev in elevi_input:
        f.write(elev + "\n")

elevi_lista = []
with open("elevi.txt", "r") as f:
    for linie in f:
        parti = linie.strip().split()
        if len(parti) == 3:
            nume, prenume, nota = parti
            elev = {
                "nume": nume,
                "prenume": prenume,
                "nota": int(nota)
            }
            elevi_lista.append(elev)

with open("elevi.json", "w") as f_json:
    json.dump(elevi_lista, f_json, indent=4)

print("\nElevi cu nota mai mare sau egală cu 8:")
for elev in elevi_lista:
    if elev["nota"] >= 8:
        print(f"{elev['nume']} {elev['prenume']} - Nota: {elev['nota']}")'''

