import sqlite3
from Pokemon_Stat_Lists_By_Generation import *

"""
create and connect to the database
"""
conn = sqlite3.connect('Pokemon.db')

"""
Connect to the cursor within SQLite
"""
c = conn.cursor()

"""
Create a table to hold all the stats from Pokemon_Stat_Lists_By_Generation
"""
c.execute("""CREATE TABLE IF NOT EXISTS PokemonBaseStats(
		Pokenumber integer,
		Name char,
		Hp real,
		Attack integer,
		Defense integer,
		Sp_Attack integer,
		Sp_Defense integer,
		Speed integer,
		Total integer,
		Average integer
		)""")

"""
Insert all the lists
"""
c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen1_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen2_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen3_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen4_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen5_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen6_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen7_List )

"""
Select, fetch, and print the information
"""
c.execute(""" SELECT * FROM PokemonBaseStats""")

c.execute("""SELECT * FROM Pokemon.db ORDER BY Hp DESC """)

print(c.fetchone())

"""
Commit changes to the database and close the connection
"""
conn.commit()
conn.close()
