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

# cursor.execute("""SELECT name,address FROM companies
#                WHERE name LIKE :name
#                ORDER BY name ASC
#                LIMIT 2""", {"name" : "%A%"})

# result = cursor.fetchall()

# print(f"\nFinal Result: {result}")


#Day 3 (Aggregation SQLITE)

cursor.execute("SELECT COUNT(*) FROM companies")
count = cursor.fetchall()
# cursor.execute("ALTER TABLE companies ADD COLUMN revenue INT")
# cursor.execute("UPDATE companies SET revenue = 10 WHERE name =:name",{"name" : "Payments"})
# cursor.execute("UPDATE companies SET revenue = 0 WHERE name =:name",{"name" : "Zoom"})
# cursor.execute("UPDATE companies SET revenue = 10 WHERE name =:name",{"name" : "Amazon"})
# cursor.execute("UPDATE companies SET revenue = 10 WHERE name =:name",{"name" : "Snapchat"})
# cursor.execute("UPDATE companies SET revenue = 0 WHERE name =:name",{"name" : "Airbnb"})
# conn.commit()

# cursor.execute("SELECT AVG(revenue) FROM companies")
# avg = cursor.fetchone()

# cursor.execute("SELECT MIN(revenue) FROM companies")
# minn = cursor.fetchone()

# cursor.execute("SELECT MAX(revenue) FROM companies")
# maxx = cursor.fetchone()

# print(f"Average: {avg}\nMinimum: {minn}\nMaximum: {maxx}")

cursor.execute("SELECT revenue FROM companies")
data = cursor.fetchone()

print(f"Data: {data}")



