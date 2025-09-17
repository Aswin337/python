'''It reads single line only'''
with open("feedback_log.txt","r") as file:
    print(file.readline().strip())   
    print(file.readline().strip())