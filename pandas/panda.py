import pandas as pd

# #A DataFrame is a table

# #Basic Syntax
# #creating a dictionary
# # data = {
#     #keys will be column name while values list will be row values
# #     "name" : ["Ali","Sara","Abdul"],
# # }

# #Turns dictionary into table
# # df = pd.DataFrame(data)

# # print(f"{df}")

# #reading the first 5 rows of table by default
# # print(df.head())

# #reading the last 5 rows of table by default
# # print(df.tail())

# #shows dataset(table) info
# # print(df.info())

# #give statistics like min,max,average,count
# # print(df.describe())

# #Selecting One Column
# # print(df["name"])

# #Selecting Multiple Column
# # print(df[["name","score"]])

# #Filtering Rows
# # high_scores = df[df["score"] > 80]

# # print(high_scores)

# #Sorting data
# # sorted_data = df.sort_values(by="score", ascending=False)

# # print(sorted_data)

# #check cell by cell if any data is null
# # df.isnull()

# # count missing values per column
# # df.isnull().sum()

# #remove rows with no data
# # df.dropna(inplace=True)

# #removing duplicates
# # df.drop_duplicates()
# # df.drop_duplicates(inplace = True) permanent removal

# #removing symbols from string
# # df["Price"] = df["Price"].str.replace("$", "")

# #changing column dattype
# # df["Price"] = df["Price"].astype(float)

# # df["Price"] = df["Price"].str.replace("$", "").astype(float)

# #reading a CSV file & storing inside variable
# #the whole csv file becomes a dataframe
# # df = pd.read_csv("students.csv")
# # print(df)


# #Tasks of PANDAS (TASK 1)

# # inventory = {
# #     "product name" : ["dryer","spoon","table","laptop"],
# #     "prices" : [10,15,12,200],
# #     "ratings" : [3.9,4.2,4.1,4.8]
# # }

# # df = pd.DataFrame(inventory)

# # print(df)

# # print(df.head(2))

# # print(df.tail(1))

# # df.info()

# # print(df.describe())

# # TASK 2 (LOAD DATA FROM CSV/EXCEL)

# # df = pd.read_csv("data.csv", encoding="latin1")

# # print(df)

# # print(df.head(3))

# # print(df.head(2))

# # df.info()

# # print(df.describe())

# # print(df["Product Name"])

# # print(df["Price"])

# # print(df[["Ratings","Product Name"]])

# # filter = df[df["Price"] > 100]

# # print(f"Products with greater than $100 Price: {filter}")

# # filter = df[df["Ratings"] > 4]

# # print(f"Products with greater than 4 Ratings: {filter}")

# # exact = df[df["Price"] ]

# # print(exact)

# # sort = df.sort_values(by="Price",ascending=True)

# # print(f"{sort}")


# # TASK 3 (DATA CLEANING)

# df = pd.read_csv("data.csv", encoding="latin1")

# # df = df.dropna()

# # df = df.drop_duplicates()

# df["Price"] = df["Price"].str.replace("$", "")
# df["Price"] = df["Price"].str.replace(",", "")
# df["Price"] = df["Price"].str.strip()
# df["Price"] = df["Price"].astype(float)

# df["Ratings"] = df["Ratings"].str.replace("stars","").astype(float)

# # print(df.head())

# # TASK 4 (DATA INSIGHTS)

# # filter = df[df["Price"] > 500]

# # print(f"Products with greater than $500 Price: {filter}")

# # filter = df[df["Price"] < 150]

# # print(f"Products with less than $150 Price: {filter}")

# # filter = df[df["Ratings"] > 4]

# # print(f"Products with greater than 4 Ratings: {filter}")

# # filter = df[df["Ratings"] < 4]

# # print(f"Products with less than 4 Ratings: {filter}")

# #sorting by price from high to low
# # sort = df.sort_values(by="Price",ascending=False)

# #printing the top 3 highest priced products
# # print(sort.head(3))

# #sorting by rartings from high to low
# # sort = df.sort_values(by="Ratings",ascending=False)

# #printing the top 3 highest rated products
# # print(sort.head(3))

# #printing statistics like avg price and ratings
# # print(df["Price"].mean())
# # print(df["Ratings"].mean())

# # TASK 5 (ANALYTICS REPORT)
# print("No of Products")
# sum = df["Product Name"].count()
# print(sum)

# print("Average Price")
# print(df["Price"].mean())

# print("\nAverage Rating")
# print(df["Ratings"].mean())

# expensive = df[df["Price"] > 500]["Product Name"].count()
# print(f"No of Expensive Products: {expensive}")

# cheap = df[df["Price"] < 150]["Product Name"].count()
# print(f"No of Cheap Products: {cheap}")

# high = df[df["Ratings"] >= 4]["Product Name"].count()
# print(f"No of High Rated Products: {high}")

# low = df[df["Ratings"] < 4]["Product Name"].count()
# print(f"No of Low Rated Products: {low}")

# print(df.sort_values(by="Price",ascending=False).head(3))

# print(df.sort_values(by="Ratings",ascending=False).head(3))

# print("\nFINAL INSIGHT:")
# print("Most products are moderately priced with a few premium items above 500.")
# print("Ratings are generally above average, showing good product quality.")
# print("Overall dataset is balanced with both budget and high-end products.")


# DAY 2 (ADVANCED PANDAS)

#Used to group departements by salary and calculate avg salary for each departement
#group = df.groupby("Department")["Salary"].mean()

#count how many times each  value appear in a column
# count = df["City"].value_counts()

#remove null rows
# clean = df.dropna()

#fill missing data
#fillna()

# # TASK 1 (GROUP BY and CATOGERY ANALYSIS)

# data = {
#     "Product": ["Laptop", "Phone", "Tablet", None, "Laptop", "Monitor"],
#     "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics", None],
#     "Price": [1200, 800, None, 150, 1200, 300],
#     "Ratings": [4.8, 4.5, 4.1, None, 4.8, 3.9]
# }

# df = pd.DataFrame(data)

# count_products = df.value_counts("Product")

# print(count_products)

# price_avg = df.groupby("Category")["Price"].mean()

# rating_avg = df.groupby("Category")["Ratings"].mean()

# print(price_avg)

# print(rating_avg)

# df = df.dropna()

# df = df.fillna("Unknown")

# print(df)

# TASK 2 (BUSINESS INSIGHT)

# temp = df.dropna()
# print("CLEANED version using DROPNA")
# print(temp)

# df.fillna(0)
# print("\nCLEANER version using FILLNA")
# print(df)

# count = df["Category"].value_counts()
# most_idx = count.idxmax()
# most_name = count.max()
# print("Frequent Category:", most_idx)
# print("No of times:", most_name)

# avg_price = df.groupby("Category")["Price"].mean()
# best_category = avg_price.idxmax()
# best_value = avg_price.max()

# print("Best Category:", best_category)
# print("Highest Average Price:", best_value)

# avg_rating = df.groupby("Category")["Ratings"].mean()
# best_category = avg_rating.idxmax()
# best_value = avg_rating.max()

# print("Best Category:", best_category)
# print("Highest Average Rating:", best_value)

# TASK 3 (ADVANCED PRODUCT INSIGHTS)

# df = df.sort_values(by="Price",ascending=False)

# print("TOP 3 MOST EXPENSIVE PRODUCTS")
# print(df.head(3))

# print("TOP 3 MOST CHEAPEST PRODUCTS")
# print(df.tail(3))

# df = df.sort_values(by="Ratings",ascending=False)

# print("TOP 3 HIGHEST RATED PRODUCTS")
# print(df.head(3))

# avg_price = df.groupby("Category")["Price"].mean()

# avg_rating = df.groupby("Category")["Ratings"].mean()

# print("AVERAGE PRICE PER CATEGORY")
# print(avg_price)

# print("AVERAGE RATING PER CATEGORY")
# print(avg_rating)

# count = df["Product"].value_counts()

# print("NO OF PRODUCTS")
# print(count)

# score = avg_price + avg_rating
# best_idx = score.idxmax()
# best_value = score.max()

# print("BEST COMBINED CATOGERY: ",best_idx)
# print("BEST COMBINE SCORE: ",best_value)

# prem_product = df[df["Price"] > df["Price"].mean()]
# low_product = df[df["Ratings"] < 4.0]

# print("PREMIUM PRODUCTS")
# print(prem_product)

# print("LOW RATED PRODUCTS")
# print(low_product)


# TASK 4 (BUSINESS REPORT DASHBOARD)
# print("----- CORE BUSINESS KPI'S -----")
# count = df["Product"].count()
# print("Total no of Products: ",count)

# avg_price = df["Price"].mean()
# print("Average Price: ",avg_price)

# avg_rating = df["Ratings"].mean()
# print("Averagee Rating: ",avg_rating)

# df = df.sort_values(by="Price",ascending=False)

# max_price = df["Price"].head(1)

# min_price = df["Price"].tail(1)

# print("Price Range: ",max_price," - ",min_price)
# print(count)

# print("\n----- CATEGORY INTELLIGENCE -----")

# av_price = df.groupby("Category")["Price"].mean()

# av_rating = df.groupby("Category")["Ratings"].mean()

# count = df["Category"].value_counts()

# print("AVERAGE PRICE PER CATEGORY")
# print(av_price)

# print("AVERAGE RATING PER CATEGORY")
# print(av_rating)

# print("NO OF PRODUCTS")
# print(count)

# print("\n----- SMART SEGMENTATION -----")

# prem_product = df[df["Price"] > df["Price"].mean()]

# stan_product = df[(df["Price"] >= df["Price"].mean() * 0.8) & (df["Price"] <= df["Price"].mean() * 1.2)]

# low_product = df[df["Price"] < df["Price"].mean() * 0.8]

# print("PREMIUM PRODUCTS: ",prem_product)
# print("STANDARD PRODUCTS: ",stan_product)
# print("LOW QUALITY PRODUCTS: ",low_product)

# print("UNUSUALLY EXPENSIVE PRODUCTS")
# print(df.head(5))

# print("UNUSUALLY CHEAP PRODUCTS")
# print(df.tail(5))





