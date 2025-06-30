'''import sqlite3


with sqlite3.connect('studenti.db') as conn:
    cursor = conn.cursor()

    # 8. Tabel Sters
    cursor.execute('DROP TABLE IF EXISTS studenti')

    # 1. Cream tabelul studenti
    cursor.execute('''
        CREATE TABLE studenti (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nume TEXT,
            varsta INTEGER
        )
    ''')

    # 2. Adaugam cel putin 5 studenti
    studenti = [
        ('Ioan', 21),
        ('Ana', 19),
        ('Bogdan', 22),
        ('Alexandra', 18),
        ('Cristina', 23)
    ]
    cursor.executemany('INSERT INTO studenti (nume, varsta) VALUES (?, ?)', studenti)

    print('\n3. Toti studentii:')
    cursor.execute('SELECT * FROM studenti')
    for row in cursor.fetchall():
        print(row)

    print('\n4. Studentii cu varsta > 20:')
    cursor.execute('SELECT * FROM studenti WHERE varsta > 20')
    for row in cursor.fetchall():
        print(row)

    print('\n5. Studentii al caror nume incepe cu litera A:')
    cursor.execute("SELECT * FROM studenti WHERE nume LIKE 'A%'")
    for row in cursor.fetchall():
        print(row)

    # 6. Crestem varsta cu 1 pentru un student
    cursor.execute('UPDATE studenti SET varsta = varsta + 1 WHERE id = 2')
    conn.commit()

    print('\n6. Studentul cu id=2 dupa cresterea varstei cu 1:')
    cursor.execute('SELECT * FROM studenti WHERE id = 2')
    print(cursor.fetchone())

    # 7. Stergem studentii cu varsta < 19
    cursor.execute('DELETE FROM studenti WHERE varsta < 19')
    conn.commit()

    print('\n7. Studentii ramasi dupa stergerea celor cu varsta < 19:')
    cursor.execute('SELECT * FROM studenti')
    for row in cursor.fetchall():
        print(row)

    # 9. Adaugam o coloana "email"
    cursor.execute('ALTER TABLE studenti ADD COLUMN email TEXT')

    # Email pentru studentul cu id=1
    cursor.execute('UPDATE studenti SET email = ? WHERE id = 1', ('andrei@gmail.com',))
    conn.commit()

    print('\n9. Studentul cu id=1 dupa adaugarea emailului:')
    cursor.execute('SELECT * FROM studenti WHERE id = 1')
    print(cursor.fetchone())'''
