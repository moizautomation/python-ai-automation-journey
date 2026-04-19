# import os
# #the list directory function is used to list all the files 
# #in a specified folder after stroing them in a lisy
# path = "C:/Users/HP/Downloads/files random"
# # print(os.listdir(path))
# #we can also use loop to just print them one by one
# # for files in os.listdir(path):
# #     print(files)

# #now shutil.move() is used to move files from one folder into another
# #for file type we use the split function
# for files in os.listdir(path):
#     #split the string into two parts at the dot
#     #move to the last index and save it into ext
#     ext = files.split('.')[-1]
#     print(ext)