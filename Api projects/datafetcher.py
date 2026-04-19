import requests
url = "https://dummyjson.com/products"
r = requests.get(url)
data = r.json()
r_list = data["products"]
for product in r_list:
    title = product["title"]
    price = product["price"]
    catogery = product["category"]
    rating = product["rating"]
    if(price > 100):
        print(f"Title: {title}\nPrice: ${price}\nCategory: {catogery}\nRating: {rating}")
