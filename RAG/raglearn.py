#Learning RAG Manually
context = ""
highest = 0
list = ["for","what","is","why","when","how","?"]
with open("data.txt","r") as f:
    data = f.readlines()
    question = input("Enter your Question: ").lower()
    question = question.split()
    for words in list:
            if words in question:
                question.remove(words)
    for line in data:
        match = 0
        lower_line = line.lower()
        for keyword in question:
            if keyword in lower_line:
                match += 1
        if(match > highest):
            highest = match
            context = line

print(context)

    
    