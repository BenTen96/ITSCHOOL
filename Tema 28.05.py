'''catalog = []

def adauga_elev():
    nume = input("Introdu numele elevului: ")
    note = input("Introdu notele (separate prin spatiu): ")
    lista_note = [int(n) for n in note.split()]
    catalog.append([nume, lista_note])
    print("Elev adăugat cu succes!\n")

def afisare_rezultate():
    for elev in catalog:
        nume = elev[0]
        note = elev[1]
        media = sum(note) / len(note)
        status = "promovat" if media >= 5 else "corigent"
        print(f"{nume} - Note: {note} - Media: {media:.2f} - {status}")
    print()

def modifica_note():
    nume = input("Introdu numele elevului pentru modificare: ")
    for elev in catalog:
        if elev[0] == nume:
            note_noua = input("Introdu noile note (separate prin spatiu): ")
            elev[1] = [int(n) for n in note_noua.split()]
            print("Note modificate!\n")
            return
    print("Elevul nu a fost găsit.\n")

def sterge_elev():
    nume = input("Introdu numele elevului de șters: ")
    for elev in catalog:
        if elev[0] == nume:
            catalog.remove(elev)
            print("Elev șters din catalog.\n")
            return
    print("Elevul nu a fost găsit.\n")

def meniu():
    while True:
        print("1. Adaugă elev")
        print("2. Afișează rezultate")
        print("3. Modifică note")
        print("4. Șterge elev")
        print("5. Exit")
        alegere = input("Alege o opțiune: ")
        if alegere == "1":
            adauga_elev()
        elif alegere == "2":
            afisare_rezultate()
        elif alegere == "3":
            modifica_note()
        elif alegere == "4":
            sterge_elev()
        elif alegere == "5":
            print("Ieșire din program.")
            break
        else:
            print("Opțiune invalidă!\n")

meniu()'''
