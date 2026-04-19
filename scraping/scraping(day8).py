# Today we are doing advanced scraping (DAY 8 & 9)
# we need to get book title,price from multiple pages
import requests
from bs4 import BeautifulSoup
# # url = requests.get("https://books.toscrape.com/")
# for page in range(1,3):

#     url = "https://books.toscrape.com/catalogue/page-" + str(page) + ".html"
#     print (url)
#     r = requests.get(url)
#     scrape = BeautifulSoup(r.text,"html.parser")
#     info = scrape.find_all("article", class_="product_pod")
#     for book in info:
#         price = book.find("p", class_="price_color")
#         title = book.h3.a["title"]
#         print(title)
#         print(price.text)

# for page in range(1,2):

#     url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
#     print (url)
#     r = requests.get(url)
#     scrape = BeautifulSoup(r.text,"html.parser")
#     tech = scrape.find_all("div", class_="card thumbnail")
#     for info in tech:
#         # caption = info.find("div",class_="caption")
#         # print(caption.text)
#         price = info.find("span", attrs={"itemprop" : "price"}).text
#         title = info.find("a", class_="title").text
#         desc = info.find("p",class_="description card-text").text
#         rating = info.find("p", attrs={"data-rating" : True})
#         #or rating = info.find("p", class_="title")
#         ratings = rating["data-rating"]
#         reviews = info.find("span", attrs={"itemprop" : "reviewCount"}).text
#         link_tag = info.find("a", attrs={"href" : True})
#         link = link_tag["href"]
#         full_link = "https://webscraper.io" + link
#         print(title)
#         print(price)
#         print(desc)
#         print(ratings)
#         print(reviews)
#         print(full_link)
for page in range(3,6):
    url = "https://books.toscrape.com/catalogue/page-" + str(page) + ".html"
    r = requests.get(url)
    scrape = BeautifulSoup(r.text,"html.parser")
    pages =  scrape.find_all("article", class_="product_pod")
    for books in pages:
        title = books.h3.a["title"]
        price = books.find("p", class_="price_color").text
        stock = books.find("p", class_="instock availability").text
        ratings = books.find("p", class_="star-rating")
        link = books.find("a", attrs={"href":True})
        l = link["href"]
        full_link = "https://books.toscrape.com/catalogue/" + l  
        print(title)
        print(price)
        print(stock)
        print(ratings.attrs["class"][1])
        print(full_link)
        

