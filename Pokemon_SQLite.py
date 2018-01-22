https://github.com/AustinCan/Portfolio_Projects.git
import sqlite3
from Pokemon_Stat_Lists_By_Generation import *

conn = sqlite3.connect('Pokemon.db')

c = conn.cursor()

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

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen1_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen2_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen3_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen4_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen5_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen6_List )

c.executemany(""" INSERT INTO PokemonBaseStats(Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", Gen7_List )

c.execute(""" SELECT * FROM PokemonBaseStats""")

'''print(c.fetchall())'''

c.execute("""SELECT * FROM Pokemon.db ORDER BY Hp DESC """)

print(c.fetchone())

conn.commit()

conn.close()