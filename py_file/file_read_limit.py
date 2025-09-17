with open("feedback_log.txt","r") as file:
    for _ in range(10):
        print(file.readline().strip())