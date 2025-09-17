'''In this method we didnt want to close it .
   File will automatically close after read it.'''
with open("file1.txt","r") as file:
    for line in file:
        print(line.strip())