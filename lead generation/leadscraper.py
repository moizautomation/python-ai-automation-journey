#Day 15 (Starting LeadScraper with csv save)
import requests
from bs4 import BeautifulSoup
import csv

# url = "https://webscraper.io/test-sites/e-commerce/allinone"

# r = requests.get(url)
# soup = BeautifulSoup(r.text,"html.parser")
# info = soup.find_all("div",class_="card thumbnail")

# with open("data.csv","w",newline="") as file:
#     writer = csv.writer(file)
#     for product in info:
#         name = product.find("a",class_="title").text
#         name = name.strip("\n\t...")

#         price = product.find("span",attrs={"itemprop" : "price"}).text
#         descr = product.find("p",class_="description card-text").text

#         writer.writerow(["Name,Price,Description"])
#         writer.writerow([name,price,descr])

#         print(f"Name:{name}\nPrice: {price}\nDescription: {descr}\n")


#Day 16-18 (Improving Scraping and saving structured Data)
#apply filtering rules

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
r = requests.get(url)
#list to save names
name_list = []
soup = BeautifulSoup(r.text,"html.parser")
info = soup.find_all("div",class_="card thumbnail")
with open("data.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Description", "Reviews"])
    for product in info:
        name = product.find("a",class_="title").text
        name = name.strip()
        #save each name in it
        found = name in name_list
        if not found:
            name_list.append(name)
        price = product.find("span",attrs={"itemprop" : "price"}).text
        descr = product.find("p",class_="description card-text").text
        descr = descr.strip()
        review = product.find("p",class_="review-count float-end").text
        review = review.strip("\n")
        reviewno = int(review.split()[0])
        
        if(reviewno > 3 and len(descr) > 10 and found == False):
            writer.writerow([name,price,descr,review])
            print(f"Name:{name}\nPrice: {price}\nDescription: {descr}\nRatings: {review}")

