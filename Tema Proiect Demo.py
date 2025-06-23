''''
# Problema 1 - Verificare parola

parola = input("Introdu parola: ")

if len(parola) < 10:
    print("Parola trebuie sa aiba cel putin 10 caractere.")
if ' ' in parola:
    print("Parola nu trebuie sa contina spatii.")
if len(parola) >= 10 and ' ' not in parola:
    print("OK")'''



'''# Problema 2 - De cate ori apare litera in cuvant

cuvant = input("Introdu un cuvant: ")
litera = input("Introdu litera cautata: ")

aparitii = cuvant.count(litera)
print(f"Litera '{litera}' apare de {aparitii} ori in cuvantul '{cuvant}'.")'''



'''# Problema 3 - Puterile lui 3 intre 200 si 300

print("Puterile lui 3 intre 200 si 300:")
putere = 1
while True:
    rezultat = 3 ** putere
    if rezultat > 300:
        break
    if rezultat >= 200:
        print(rezultat)
    putere += 1'''



'''# Problema 4 - Suma de la 1 pana la un numar citit (FOR & WHILE)

n = int(input("Introdu un numar pentru suma: "))

# FOR
suma_for = 0
for i in range(1, n + 1):
    suma_for += i
print(f"Suma (FOR): {suma_for}")

# WHILE
suma_while = 0
i = 1
while i <= n:
    suma_while += i
    i += 1
print(f"Suma (WHILE): {suma_while}")'''




'''# Problema 5 - Numaratoare inversa (FOR & WHILE)

n = int(input("Problema 5 - Introdu un numar pentru numaratoare inversa: "))

# FOR
print("Numaratoare inversa (FOR):")
for i in range(n, -1, -1):
    print(i)

# WHILE
print("Numaratoare inversa (WHILE):")
while n >= 0:
    print(n)
    n -= 1'''





'''# Problema 6 - Suma pana la un numar (FOR & WHILE)

n = int(input("Introdu un numar pentru suma: "))

# FOR
suma_for = sum(range(1, n + 1))
print(f"Suma (FOR): {suma_for}")

# WHILE
suma_while = 0
i = 1
while i <= n:
    suma_while += i
    i += 1
print(f"Suma (WHILE): {suma_while}")'''