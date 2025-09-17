feedback=input("Enter your feedback :")
with open("feedback_log.txt","a") as file:
    file.write(feedback.strip()+"\n")
print("Thanks, for your Feedback !")