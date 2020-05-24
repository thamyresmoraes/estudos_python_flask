import sqlite3

connection = sqlite3.connect('travel.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
nome text, estrelas real, diaria real, cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES ('alpha', 'Alpha Hotel', 4.3, 345.30, 'Rio de Janeiro')"

cursor.execute(create_table)
cursor.execute(cria_hotel)

connection.commit()
connection.close()
