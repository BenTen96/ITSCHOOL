'''angajati = []

def validare_cnp(cnp):
    return cnp.isdigit() and len(cnp) == 13

def validare_varsta(varsta):
    return varsta.isdigit() and int(varsta) >= 18

def validare_salar(salar):
    return salar.isdigit() and int(salar) >= 4050

def cauta_angajat_dupa_cnp(cnp):
    for angajat in angajati:
        if angajat["cnp"] == cnp:
            return angajat
    return None

# 1) Adaugare angajat
def adauga_angajat():
    cnp = input("CNP: ")
    if not validare_cnp(cnp):
        print("CNP invalid!")
        return
    if cauta_angajat_dupa_cnp(cnp):
        print("Angajatul există deja.")
        return

    nume = input("Nume: ")
    prenume = input("Prenume: ")
    varsta = input("Vârstă: ")
    if not validare_varsta(varsta):
        print("Vârstă invalidă!")
        return
    salar = input("Salariu: ")
    if not validare_salar(salar):
        print("Salariu invalid!")
        return
    departament = input("Departament: ")
    senioritate = input("Senioritate (junior/mid/senior): ").lower()
    if senioritate not in ["junior", "mid", "senior"]:
        print("Senioritate invalidă!")
        return

    angajati.append({
        "cnp": cnp,
        "nume": nume,
        "prenume": prenume,
        "varsta": int(varsta),
        "salar": int(salar),
        "departament": departament,
        "senioritate": senioritate
    })
    print("Angajat adăugat cu succes!")

# 2) Cautare angajat
def cautare_angajat():
    cnp = input("Introdu CNP-ul angajatului: ")
    angajat = cauta_angajat_dupa_cnp(cnp)
    if angajat:
        print(angajat)
    else:
        print("Angajatul nu a fost găsit.")

# 3) Modificare date angajat
def modificare_angajat():
    cnp = input("CNP angajat de modificat: ")
    angajat = cauta_angajat_dupa_cnp(cnp)
    if not angajat:
        print("Angajatul nu a fost găsit.")
        return
    print("")
    nume = input(f"Nume nou ({angajat['nume']}): ") or angajat['nume']
    prenume = input(f"Prenume nou ({angajat['prenume']}): ") or angajat['prenume']
    varsta = input(f"Vârstă nouă ({angajat['varsta']}): ") or angajat['varsta']
    salar = input(f"Salariu nou ({angajat['salar']}): ") or angajat['salar']
    departament = input(f"Departament nou ({angajat['departament']}): ") or angajat['departament']
    senioritate = input(f"Senioritate nouă ({angajat['senioritate']}): ") or angajat['senioritate']

    # Validări
    if not validare_varsta(str(varsta)) or not validare_salar(str(salar)):
        print("Date invalide.")
        return

    angajat.update({
        "nume": nume,
        "prenume": prenume,
        "varsta": int(varsta),
        "salar": int(salar),
        "departament": departament,
        "senioritate": senioritate
    })
    print("Datele au fost actualizate.")

# 4) Stergere angajat
def sterge_angajat():
    cnp = input("CNP angajat de șters: ")
    angajat = cauta_angajat_dupa_cnp(cnp)
    if angajat:
        angajati.remove(angajat)
        print("Angajat șters.")
    else:
        print("Angajatul nu a fost găsit.")

# 5) Afisare angajati
def afiseaza_angajati():
    if not angajati:
        print("Nu există angajați.")
    for a in angajati:
        print(a)

# 6) Cost total salarii
def cost_total_salarii():
    total = sum(a["salar"] for a in angajati)
    print(f"Cost total salarii: {total} RON")

# 7) Cost total salarii pe departament
def cost_total_salarii_departament():
    departament = input("Introduceți departamentul: ")
    total = sum(a["salar"] for a in angajati if a["departament"] == departament)
    print(f"Cost salarii departament {departament}: {total} RON")

# 8) Fluturaș salariu
def fluturas_salar():
    cnp = input("CNP angajat: ")
    angajat = cauta_angajat_dupa_cnp(cnp)
    if not angajat:
        print("Angajatul nu a fost găsit.")
        return
    brut = angajat["salar"]
    cas = 0.10 * brut
    cass = 0.25 * brut
    impozit = 0.10 * (brut - cas - cass)
    net = brut - cas - cass - impozit
    print(f"""
Fluturaș Salar - {angajat['nume']} {angajat['prenume']}
Brut: {brut} RON
CAS (10%):'''
