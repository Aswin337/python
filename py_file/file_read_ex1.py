with open("feedback_log.txt","r") as file:
    while True:
        line=file.readline().strip()
        if not line:
            break
        if "bad" in line.lower():
            print("Word Bad Found :",line)