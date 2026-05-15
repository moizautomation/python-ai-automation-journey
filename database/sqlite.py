import sqlite3

#open/connect to the database
conn = sqlite3.connect("test.db")

#create a cursor to execute commands in the database
cursor = conn.cursor()

print("Database Connected")

#creating the database
cursor.execute("""
CREATE TABLE IF NOT EXISTS companies(
               Id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               address TEXT
    )
""")
conn.commit()

#inserting data row by row
cursor.execute("INSERT INTO companies (name,address) VALUES(:name,:address)",{"name" : "Stripe", "address" : "Fintech"})
cursor.execute("INSERT INTO companies (name,address) VALUES(:name,:address)",{"name" : "Snapchat", "address" : "America"})
cursor.execute("INSERT INTO companies (name,address) VALUES(:name,:address)",{"name" : "Amazon", "address" : "Pakistan"})
cursor.execute("INSERT INTO companies (name,address) VALUES(:name,:address)",{"name" : "Zoom", "address" : "Australia"})
cursor.execute("INSERT INTO companies (name,address) VALUES(:name,:address)",{"name" : "AirBnb", "address" : "Newzeland"})
conn.commit()

cursor.execute("SELECT * FROM companies WHERE name=:name AND address=:address",{"name" : "Stripe","address" : "Fintech"})
all_data = cursor.fetchall()

print(all_data)

cursor.execute("UPDATE companies SET name=:name WHERE address=:address",{"name" : "Payments","address" : "Fintech"})
conn.commit()

cursor.execute("DELETE FROM companies where name=:name AND address=:address",{"name" : "Zoom","address" : "Australia"})
#commiting the change into the database
conn.commit()

conn.close()

