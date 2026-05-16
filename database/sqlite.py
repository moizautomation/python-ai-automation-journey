import sqlite3

# #open/connect to the database
# conn = sqlite3.connect("test.db")

# #create a cursor to execute commands in the database
# cursor = conn.cursor()

# print("Database Connected")

# #creating the database
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS companies(
#                Id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT,
#                address TEXT
#     )
# """)
# conn.commit()

# #inserting data row by row
# cursor.execute("INSERT INTO companies (name,address) VALUES(:name,:address)",{"name" : "Stripe", "address" : "Fintech"})
# cursor.execute("INSERT INTO companies (name,address) VALUES(:name,:address)",{"name" : "Snapchat", "address" : "America"})
# cursor.execute("INSERT INTO companies (name,address) VALUES(:name,:address)",{"name" : "Amazon", "address" : "Pakistan"})
# cursor.execute("INSERT INTO companies (name,address) VALUES(:name,:address)",{"name" : "Zoom", "address" : "Australia"})
# cursor.execute("INSERT INTO companies (name,address) VALUES(:name,:address)",{"name" : "AirBnb", "address" : "Newzeland"})
# conn.commit()

#searching for data in all the rows, exact match
# * means select all columns
# cursor.execute("SELECT * FROM companies WHERE name=:name AND address=:address",{"name" : "Stripe","address" : "Fintech"})
# all_data = cursor.fetchall()

# print(all_data)

#updating specific record in the database
# cursor.execute("UPDATE companies SET name=:name WHERE address=:address",{"name" : "Payments","address" : "Fintech"})
# conn.commit()

#deleting some specific record 
# cursor.execute("DELETE FROM companies where name=:name AND address=:address",{"name" : "Zoom","address" : "Australia"})
# #commiting the change into the database
# conn.commit()

#closing the connection with the database
# conn.close()


#Day 2 - learning sqlites basics (LIKE, ORDER BY, LIMIT,BETTER SELECT USAGE)
conn = sqlite3.connect("test.db")

cursor = conn.cursor()

print("Database Connected")

# cursor.execute("SELECT name,address FROM companies where name LIKE :name",{"name" : "Pay%"})

# stripe = cursor.fetchall()

# cursor.execute("SELECT name,address FROM companies where name LIKE :name",{"name" : "%ir%"})

# zoom = cursor.fetchall()

# cursor.execute("SELECT name,address FROM companies where name LIKE :name",{"name" : "%zon"})

# amazon = cursor.fetchall()

# print(f"First: {stripe}\nSecond: {zoom}\nThird: {amazon}")

# cursor.execute("SELECT * FROM companies ORDER BY name ASC LIMIT 2")
# row = cursor.fetchall()
# print(f"Ascending Order: {row}")

cursor.execute("""SELECT name,address FROM companies
               WHERE name LIKE :name
               ORDER BY name ASC
               LIMIT 2""", {"name" : "%A%"})

result = cursor.fetchall()

print(f"\nFinal Result: {result}")

