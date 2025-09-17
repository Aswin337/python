import time
from datetime import datetime
def task():
    with open("date_while.txt","+a") as f:
        f.write(f"Script at {datetime.now()}")
    print(f"Task ran at {datetime.now()}")

while True:
    task()
    time.sleep(10)