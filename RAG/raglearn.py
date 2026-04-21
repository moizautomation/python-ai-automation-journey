#Learning RAG Manually

question = input("Enter your Question: ")
word = question

with open("data.txt","r") as f:
    line = f.readline()
    if(word == line):
        context = word