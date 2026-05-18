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
conn = sqlite3.connect("tesst.db")

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


#Day 3 (Aggregation SQLITE Learning how to group similar data,find min,max,avg,sum etc and apply conditions on group using having)

# cursor.execute("SELECT COUNT(*) FROM companies")
# count = cursor.fetchall()
# cursor.execute("ALTER TABLE companies ADD COLUMN revenue INT")
# cursor.execute("UPDATE companies SET revenue = 10 WHERE name =:name",{"name" : "Payments"})
# cursor.execute("UPDATE companies SET revenue = 0 WHERE name =:name",{"name" : "Zoom"})
# cursor.execute("UPDATE companies SET revenue = 10 WHERE name =:name",{"name" : "Amazon"})
# cursor.execute("UPDATE companies SET revenue = 10 WHERE name =:name",{"name" : "Snapchat"})
# cursor.execute("UPDATE companies SET revenue = 0 WHERE name =:name",{"name" : "Airbnb"})
# conn.commit()

# cursor.execute("SELECT SUM(revenue) FROM companies")
# sum = cursor.fetchone()

# cursor.execute("SELECT AVG(revenue) FROM companies")
# avg = cursor.fetchone()

# cursor.execute("SELECT MIN(revenue) FROM companies")
# minn = cursor.fetchone()

# cursor.execute("SELECT MAX(revenue) FROM companies")
# maxx = cursor.fetchone()

# print(f"Sum: {sum}\nAverage: {avg}\nMinimum: {minn}\nMaximum: {maxx}")

#Select means choosing the data we want to display
# cursor.execute("SELECT revenue, Count (*) FROM companies GROUP BY revenue")
# data = cursor.fetchall()

# print(f"Data: {data}")

# cursor.execute("""CREATE TABLE IF NOT EXISTS employee(
#                Id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name TEXT,
#                salary INTEGER,
#                address TEXT
#                )""")

# cursor.execute("INSERT INTO employee(name,salary,address) VALUES(:name,:salary,:address)",{"name" : "Abdul","salary" : 10, "address" : "Pakistan"})
# cursor.execute("INSERT INTO employee(name,salary,address) VALUES(:name,:salary,:address)",{"name" : "Abd","salary" : 300, "address" : "Pakistan"})
# cursor.execute("INSERT INTO employee(name,salary,address) VALUES(:name,:salary,:address)",{"name" : "Moiz","salary" : 60, "address" : "Canada"})
# cursor.execute("INSERT INTO employee(name,salary,address) VALUES(:name,:salary,:address)",{"name" : "Abd","salary" : 100, "address" : "USA"})
# conn.commit()

# cursor.execute("SELECT name, COUNT(*) FROM employee GROUP BY name HAVING COUNT(*) > 1")

# data = cursor.fetchall()

# print(f"Grouped Data: {data}")

# cursor.execute("SELECT SUM(salary) FROM employee")
# total = cursor.fetchone()

# cursor.execute("SELECT AVG(salary) FROM employee")
# avg = cursor.fetchone()

# cursor.execute("SELECT MIN(salary) FROM employee")
# min = cursor.fetchone()

# cursor.execute("SELECT MAX(salary) FROM employee")
# max = cursor.fetchone()

# print(f"Total Salary: {total}\nAverage Salary: {avg}\nMin Salary: {min}\nMax Salary: {max}")

#Going to select the salary column and arrange it in ascending order and will show top 3 only
cursor.execute("SELECT salary FROM employee  ORDER BY salary DESC LIMIT 3")

ordered = cursor.fetchall()

cursor.execute("SELECT MAX(salary) FROM employee")
max_salary = cursor.fetchone()

cursor.execute("SELECT MIN(salary) FROM employee")
min_salary = cursor.fetchone()

print(f"Data sorted by salary: {ordered}\nMinimum Salary: {min_salary}\nMaximum Salary: {max_salary}")







