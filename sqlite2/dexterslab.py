import sqlite3

conn = sqlite3.connect("dexters_lab.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Characters (
        character_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Inventions (
        invention_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS CharacterInventions (
        id INTEGER PRIMARY KEY,
        character_id INTEGER,
        invention_id INTEGER,
        FOREIGN KEY (character_id) REFERENCES Characters(character_id),
        FOREIGN KEY (invention_id) REFERENCES Inventions(invention_id)
    )
''')

cursor.execute("INSERT INTO Characters (name) VALUES ('Dexter')")
cursor.execute("INSERT INTO Characters (name) VALUES ('Dee Dee')")
cursor.execute("INSERT INTO Inventions (name) VALUES ('Dexo-Transformer')")
cursor.execute("INSERT INTO Inventions (name) VALUES ('Invisibility Helmet')")

cursor.execute("INSERT INTO CharacterInventions (character_id, invention_id) VALUES (1, 1)")
cursor.execute("INSERT INTO CharacterInventions (character_id, invention_id) VALUES (1, 2)")
cursor.execute("INSERT INTO CharacterInventions (character_id, invention_id) VALUES (2, 2)")

conn.commit()
conn.close()

print("Database created and populated successfully.")

