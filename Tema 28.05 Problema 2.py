'''def detecteaza_operator():
    numar = input("Introdu numărul de telefon: ")

    numar = numar.replace(" ", "").replace("-", "")
    if numar.startswith("+40"):
        numar = "0" + numar[3:]
    elif numar.startswith("0040"):
        numar = "0" + numar[4:]

    if len(numar) != 10 or not numar.isdigit() or not numar.startswith("0"):
        print("Număr invalid!\n")
        return

    prefix = numar[2:4]

    vodafone = ["72", "73"]
    orange = ["74", "75"]
    telekom = ["76", "78"]
    digi = ["77"]

    operatori = [
        ["Vodafone", vodafone],
        ["Orange", orange],
        ["Telekom", telekom],
        ["Digi", digi]
    ]

    for operator in operatori:
        if prefix in operator[1]:
            print(f"Numărul aparține rețelei: {operator[0]}\n")
            return

    print("Operator necunoscut.\n")

while True:
    detecteaza_operator()
    cont = input("Vrei să verifici alt număr? (da/nu): ")
    if cont.lower() != "da":
        break'''
