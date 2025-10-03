from datetime import datetime
with open("text_time.txt","a") as f:
    f.write(f"script run  at {datetime.now()} \n")