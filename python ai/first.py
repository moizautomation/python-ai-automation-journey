#string immutable(values cannot be changed)
# str = "abdul"
# print(str[-3:-1])
# print(str.endswith("ul")) #true if string ends with ul
# print(str.capitalize()) #capitalize the first character, does not change the original string
# print(str.replace('a', 'p')) #to replace a character or word
# print(str.find('l')) #return index of the character
# print(str.count('a')) #return count of the word or character in the string


# name = "She had 15$ out of which she spent 12$ and only 3$ were left"
# print(name.count("$"))

# #list it is mutable(values can be changed unlike strings)
# list = [90, 34, 43]
# list.append(3)
# list.sort()  #sort in ascending order
# list.sort(reverse=True) #sort in descending order
# list.reverse()
# list.insert(0, 3) #(index, value) add value at a specific index
# list.remove(3) #remove the value first occurence
# list.pop(1) #(index) deletes a value at a particular index
# print(list)

# #tuple immutable(values cannot be changed like strings)
# tuple = (1,2,3)
# print(tuple)
# tuplesingle = (1,) #always use comma even if there is a single value
# print(tuplesingle)
# print(tuple.index(2)) #finds the elemnt and return its index
# print(tuple.count(1))

# name1 = input("Enter name of First movie: ")
# name2 = input("Enter name of Second movie: ")
# name3 = input("Enter name of Third movie: ")

# movies = [name1, name2, name3]
# print(movies)

# list1 = [1,"abc","abc",1]
# list = [1,2,3,2,1]
# list2 = list1
# list1.reverse()
# if(list1 == list2):
#     print("List is Palindrome")
# else:
#     print("List is not Palindrome")

# #dictionary
# info = {
#     "name" : "Moiz",
#     "Rollno" : 252177,
# }
# print(info)
# #for accessing any Key
# info["name"] = "Abdul"
# info["surname"] = "Moiz" #will make new key value pair surname
# print(info["name"])
# print(info["surname"])

#nested dictionary
# dict = {
#     "name" : "Abdul Moiz",
#     "score" : {
#         "physics" : 34,
#         "maths" : 35,
#         "chem " : 37,
#     } 
# }
# print(dict.keys()) #return all dictionary keys of outer layers not ensted one
# print(list(dict.keys()))
# print(len(dict))
# print(dict.values()) #return all values
# print(list(dict.values()))
# print(dict.items()) #return all key-value pair in the form of tuple
# print(dict.get("name")) #return the value of the key specified
# dict.update({"city" : "faisalabad"})
# print(dict)

#Sets

# set2 = {1,2,3,4}
# set = set() #empty set
# set.add(2)  #adds a value
# set.remove(2)   #removes a value
# # set.clear() #empties the whole set
# # set.pop() #removes a random value
# print(set.union(set2))
# print(set.intersection(set2))

# students = {"Python", "Java","Javascript","C++","C"}
# print(len(students))

# maths = int(input("Enter your Maths marks: "))
# physics = int(input("Enter your Physicss marks: "))
# comp = int(input("Enter your Comp marks: "))

# marks = {}
# marks.update({"marks": [maths, physics, comp]})
# print(marks)

#While loop
# i = 1
# n = int(input("Enter a number: "))
# while i <= 10:
#     print(n*i)
#     i+=1
# list = [1,4,9,16,25,36,49,64,81,100]
# x = int(input("Enter no to search: "))
# length = len(list)
# i = 0
# while i < length:
#     if(list[i] == x):
#         print("Number Found")
#     i += 1

# #for loop
# list = [1,2,3]
# for el in list:
#     print(el)
# idx=2
# for el in range(1,11): #range(start,stop,step) not include stop value
#     print(el*idx)

# n = int(input("How many number you want sum of: "))
# sum = 1
# # while i <= n:
# #     sum += i
# #     i+=1
# # print(sum)
# n = 5
# for i in range(1,n+1):
#     sum *= i
# print(sum)

# def calc_sum(a,b):
#     print(a+b)

# calc_sum(3,2)
#recursion
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

#file opening
# f = open("demo.txt","r")
# data = f.read()       #(can give number of character in here as well)
# d = f.readline() #only read one line
# print(d)
# f.close()
# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)
#for removing files
import os
os.remove("demo.txt")
