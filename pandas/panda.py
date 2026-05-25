import pandas as pd

#A DataFrame is a table

#Basic Syntax
#creating a dictionary
# data = {
    #keys will be column name while values list will be row values
#     "name" : ["Ali","Sara","Abdul"],
# }

#Turns dictionary into table
# df = pd.DataFrame(data)

# print(f"{df}")

#reading the first 5 rows of table by default
# print(df.head())

#reading the last 5 rows of table by default
# print(df.tail())

#shows dataset(table) info
# print(df.info())

#give statistics like min,max,average,count
# print(df.describe())

#Selecting One Column
# print(df["name"])

#Selecting Multiple Column
# print(df[["name","score"]])

#Filtering Rows
# high_scores = df[df["score"] > 80]

# print(high_scores)

#Sorting data
# sorted_data = df.sort_values(by="score", ascending=False)

# print(sorted_data)

#check cell by cell if any data is null
# df.isnull()

# count missing values per column
# df.isnull().sum()

#remove rows with no data
# df.dropna(inplace=True)

#removing duplicates
# df.drop_duplicates()
# df.drop_duplicates(inplace = True) permanent removal

#removing symbols from string
# df["Price"] = df["Price"].str.replace("$", "")

#changing column dattype
# df["Price"] = df["Price"].astype(float)

# df["Price"] = df["Price"].str.replace("$", "").astype(float)

#reading a CSV file & storing inside variable
#the whole csv file becomes a dataframe
# df = pd.read_csv("students.csv")
# print(df)


#Tasks of PANDAS (TASK 1)

# inventory = {
#     "product name" : ["dryer","spoon","table","laptop"],
#     "prices" : [10,15,12,200],
#     "ratings" : [3.9,4.2,4.1,4.8]
# }

# df = pd.DataFrame(inventory)

# print(df)

# print(df.head(2))

# print(df.tail(1))

# df.info()

# print(df.describe())

# TASK 2 (LOAD DATA FROM CSV/EXCEL)

# df = pd.read_csv("data.csv", encoding="latin1")

# print(df)

# print(df.head(3))

# print(df.head(2))

# df.info()

# print(df.describe())

# print(df["Product Name"])

# print(df["Price"])

# print(df[["Ratings","Product Name"]])

# filter = df[df["Price"] > 100]

# print(f"Products with greater than $100 Price: {filter}")

# filter = df[df["Ratings"] > 4]

# print(f"Products with greater than 4 Ratings: {filter}")

# exact = df[df["Price"] ]

# print(exact)

# sort = df.sort_values(by="Price",ascending=True)

# print(f"{sort}")


# TASK 3 (DATA CLEANING)

df = pd.read_csv("data.csv", encoding="latin1")

df = df.dropna()

df = df.drop_duplicates()

df["Price"] = df["Price"].str.replace("$","").astype(float)

df["Ratings"] = df["Ratings"].str.replace("stars","").astype(float)

print(df.head())

# TASK 4 (DATA INSIGHTS)

filter = df[df["Price"] > 500]

print(f"Products with greater than $500 Price: {filter}")

filter = df[df["Price"] < 150]

print(f"Products with less than $150 Price: {filter}")

filter = df[df["Ratings"] > 4]

print(f"Products with greater than 4 Ratings: {filter}")

filter = df[df["Ratings"] < 4]

print(f"Products with less than 4 Ratings: {filter}")

#sorting by price from high to low
sort = df.sort_values(by="Price",ascending=False)

#printing the top 3 highest priced products
print(sort.head(3))

#sorting by rartings from high to low
sort = df.sort_values(by="Ratings",ascending=False)

#printing the top 3 highest rated products
print(sort.head(3))

#printing statistics like avg price and ratings
print(df["Price"].mean())
print(df["Ratings"].mean())