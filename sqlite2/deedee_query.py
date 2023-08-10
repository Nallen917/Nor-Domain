import sqlite3

def query_database(query):
    conn = sqlite3.connect("dexters_lab.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

ooooooh_1 = "SELECT * FROM Characters"
What_do_you_want_woman_2 = "SELECT * FROM Inventions"
Dee_DEE_3 = """SELECT Characters.name, Inventions.name FROM Characters
               JOIN CharacterInventions ON Characters.character_id = CharacterInventions.character_id
               JOIN Inventions ON CharacterInventions.invention_id = Inventions.invention_id"""

result_1 = query_database(ooooooh_1)
result_2 = query_database(What_do_you_want_woman_2)
result_3 = query_database(Dee_DEE_3)

print("Characters:")
for row in result_1:
    print(row)

print("\nInventions:")
for row in result_2:
    print(row)

print("\nCharacter-Invention Relationships:")
for row in result_3:
    print(row)
