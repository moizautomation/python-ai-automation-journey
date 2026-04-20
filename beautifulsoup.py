#Day 6 (Learning Beautifulsoap)
#this is used to extract information from a website like news from a newspaper website.
import requests
from bs4 import BeautifulSoup
# r = requests.get("https://www.google.com")
# #read and save the html in soup
# soup = BeautifulSoup(r.text,"html.parser")
# #pretify is added so printed html look clean
# # tag = soup.title
# #to find some tag or anything
# tag = soup.find_all("p")
# #you can modify the tag by
# # tag.string = "hello"
# print(tag)

# r = requests.get("https://quotes.toscrape.com")
# soup = BeautifulSoup(r.text,"html.parser")
# quotes = soup.find("span", class_="text")
# print(quotes)

#Mini Simple Scraping Tool (Price, Title)
# r = requests.get("https://books.toscrape.com")
# info = BeautifulSoup(r.text, "html.parser")
# book = info.find_all("article", class_="product_pod")
# for book in book:
#     title = book.h3.a["title"]
#     price = book.find("p", class_= "price_color")
#     print(title)
#     print(price.text)

# #Quote scraper
# r = requests.get("https://quotes.toscrape.com")
# info = BeautifulSoup(r.text, "html.parser")
# quotes = info.find_all("div", class_= "quote")
# for quote in quotes:
#     # print(quote)
#     quot = quote.text
#     author = quote.find("small", class_= "author").text
#     print(quot)
#     print(author)


