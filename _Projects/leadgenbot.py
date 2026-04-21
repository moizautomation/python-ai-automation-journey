#Lead Generation Bot Project
import requests
from bs4 import BeautifulSoup
import csv

#empty set to store the data of each product
#used for duplication check
keys = set()
with open("data.csv","w",newline="") as file:
    writer = csv.writer(file)

    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops" 
    r = requests.get(url)

    #getting the html thorough beautiful soup
    soup = BeautifulSoup(r.text,"html.parser")
    #finding the main divs containing all product data
    info = soup.find_all("div",class_="card thumbnail")

    #writing the header
    writer.writerow(["Product Name","Price","Description","Ratings","Link"])

    #going through each div through loop
    for product in info:
        #finding the name
        name = product.find("a",class_="title").text
        #stripping garbage values like \n from name
        name = name.strip()

        #extracting price
        price = product.find("span",attrs={"itemprop" : "price"}).text
        
        #extracting description
        desc = product.find("p",class_="description card-text").text
        #stripping garbage values like \n from description
        desc = desc.strip()

        #finding ratings
        rating = product.find("p",attrs={"data-rating" : True})
        ratings = rating.attrs["data-rating"] + " " + "stars"

        link = product.find("a",attrs={"href" : True})
        #making the complete link of that product
        full_link = "https://webscraper.io" + link.attrs["href"]

        #Making the unique key to identify each product
        key = name + "|" + price + "|" + link.attrs["href"]

        # if(price != "" and len(name) != 0 and key not in keys):, its cleaner version is below
        if name and price and key not in keys:
            keys.add(key)
            writer.writerow([name,price,desc,ratings,full_link])