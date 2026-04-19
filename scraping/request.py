#Day 4 and 5(Learning how to fetch data from website)
import requests

# response = requests.get("https://www.google.com")
# print(response.headers)
#print(response.ok) return true when response is okay and false when there is an error
# print(dir(response)) #to show all the available functions we can perfrom

# url = "https://httpbin.org/post"
#JSON
# data = {
#     "username" : "Moiz",
#     "password" : 123
# }
# response = requests.post(url, data = data)
# print(response.text)

#For picture fetch and save
# r = requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc9APxkj0xClmrU3PpMZglHQkx446nQPG6lA&s")
# #open file in wb(write byte mode) and write image bytes in the file to save the image
# with open('bytes.png','wb') as f:
#     f.write(r.content)

#how to pass paramter with url like /get?page=2count=25, we can do it with dictionary help
# payload = {
#     "page" : 2,
#     "count" : 25
# }
# r = requests.get("https://httpbin.org/get",params = payload)
# print(r.text)
# #it will make the url itself
# print(r.url)

#mini challenge (Joke Fetcher)


while True:
    r = requests.get("https://official-joke-api.appspot.com/random_joke")
    if r.status_code == 200:
         response = r.json()
         print(response['setup'])
         print(response['punchline'])
    else:
         print("Error ",r.status_code)

    again = input("\nDo you want another joke? (yes/no): ")
    if again.lower() != "yes":
        break



