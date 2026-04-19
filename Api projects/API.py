#Learning API's (Day 10 & Day 11)
import requests
# r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# #this below line will return json in form of 
# #a python dictionary whose elements can be accessed
# #through []
# data = r.json()
# userId = data["userId"]
# id = data["id"]
# title = data["title"]
# body = data["body"]
# print("User Id:",userId) 
# print("Id:",id)
# print("Title:",title)
# print("Body:",body)

# url = "https://jsonplaceholder.typicode.com/posts"
# r = requests.get(url)
# if(r.status_code == 200):
#     data = r.json()

#     for posts in data[:8]:
#         userid = posts["userId"]
#         post_id = posts["id"]
#         title = posts["title"]
#         body = posts["body"]
#         print(f"User Id:{userid}") 
#         print(f"Id:{post_id}")
#         print(f"Title:{title}")
#         print(f"Body:{body}")
# else:
#     print("Request Failed!!!")

#nested api aceess
# url = "https://jsonplaceholder.typicode.com/users"
# r = requests.get(url)
# if(r.status_code == 200):
#     data = r.json()
#     for user in data[:10]:
#         name = user["name"]
#         email = user["email"]
#         city = user["address"]["city"]
#         street = user["address"]["street"]
#         company_name = user["company"]["name"]
#         print(f"Name:{name}")
#         print(f"Email:{email}")
#         print(f"Address:{street}, {city}")
#         print(f"Company Name:{company_name}")
#         print("\n")
# else:
#     print("Request Failed!!")

#Day 11 Task 1
# users = requests.get("https://dummyjson.com/users",timeout=5)
# post = requests.get("https://dummyjson.com/posts",timeout=5)
# if(users.status_code == 200 and post.status_code == 200):
#     user_data = users.json()
#     user_list = user_data["users"]
#     post_data = post.json()
#     post_list = post_data["posts"]
#     for user in user_list:
#         firstname = user["firstName"]
#         lastname = user["lastName"]
#         name = firstname + " " + lastname
#         email = user["email"]
#         print(f"Name: {name}")
#         print(f"Email: {email}")
#         post_no = 0
#         titles =[]
#         for posts in post_list:
#             if(user["id"] == posts["userId"]):
#                   post_no+=1
#                   titles.append(posts["title"])

#         print("Total Posts:", post_no)

#         print("First 3 Titles:")
#         for t in titles[:3]:
#             print("-", t)
# else:
#     print("Request Failed!!!")

#Day 11 Task 2
# for post in range(1,6):
#     url = "https://dummyjson.com/posts?userId=" + str(post)
#     r = requests.get(url)
#     r_data = r.json()
#     userId = post
#     r_list = r_data["posts"]
#     post_no = 0
#     for posts in r_list:
#         if(posts["userId"] == userId):
#             post_no+=1
#     print(f"User Id: {userId}\nNo of Posts: {post_no}")

#Day 12 Task 3 API scraping
bestuser = 0
highest = 0
for user in range(1,6):
    url = "https://dummyjson.com/posts?userId=" + str(user) 
    r = requests.get(url)
    data = r.json()
    r_list = data["posts"]
    postno = 0
    for post in r_list:
        if(post["userId"] == user):
            postno+=1
    if(postno > highest):
        highest = postno
        bestuser = user

print(f"User with most posts: {bestuser}")
print(f"Most no of posts: {highest}")
        


                




        
