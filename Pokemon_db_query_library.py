import sqlite3

conn = sqlite3.connect('Pokemon.db')

c = conn.cursor()

stat = input("Enter a stat: Pokenumber, Name, Hp, Attack, Defense, Sp_Attack, Sp_Defense, Speed, Total, Average")
if stat == "Pokenumber":
	c.execute("""SELECT * FROM PokemonBaseStats ORDER BY Pokenumber DESC """)
	print(c.fetchall())
elif stat == "Name":
	c.execute("""SELECT * FROM PokemonBaseStats ORDER BY Name DESC  """)
	print(c.fetchall())
elif stat == "Hp":
	c.execute("""SELECT * FROM PokemonBaseStats ORDER BY Hp DESC  """)
	print(c.fetchall())
elif stat == "Attack":
	c.execute("""SELECT * FROM PokemonBaseStats ORDER BY Attack DESC  """)
	print(c.fetchall())
elif stat == "Defense":
	c.execute("""SELECT * FROM PokemonBaseStats ORDER BY Defense DESC  """)
	print(c.fetchall())
elif stat == "Sp_Attack":
	c.execute("""SELECT * FROM PokemonBaseStats ORDER BY Sp_Attack DESC  """)
	print(c.fetchall())
elif stat == "Sp_Defense":
	c.execute("""SELECT * FROM PokemonBaseStats ORDER BY Sp_Defense DESC  """)
	print(c.fetchall())
elif stat == "Speed":
	c.execute("""SELECT * FROM PokemonBaseStats ORDER BY Speed DESC  """)
	print(c.fetchall())
elif stat == "Total":
	c.execute("""SELECT * FROM PokemonBaseStats ORDER BY Total DESC  """)
	print(c.fetchall())
elif stat == "Average":
	c.execute("""SELECT * FROM PokemonBaseStats ORDER BY Average DESC  """)
	print(c.fetchall())
else: print("That wasn't an option")
