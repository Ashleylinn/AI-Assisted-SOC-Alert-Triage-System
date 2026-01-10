import csv
from datetime import datetime, timedelta
import random

users = ["Ashley", "Mandy", "Jerry"]
locations = ["Taiwan", "USA", "Canada"]
ips = ["192.168.1.10", "192.168.1.11", "10.0.0.5"]

logs = []
start_time = datetime.now()

# normal login activity
for i in range(20):
    logs.append([
        (start_time + timedelta(minutes=i)).isoformat(),
        random.choice(users),
        random.choice(ips),
        random.choice(locations),
        "success"
    ])

# suspicious activity login failed
for i in range(10):
    logs.append([
        (start_time + timedelta(minutes=30 + i)).isoformat(),
        "Daniel",
        "203.0.113.50",
        "Japan",
        "failure"
    ])

with open("login_logs.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "user", "ip", "location", "result"])
    writer.writerows(logs)

print("login_logs.csv created")
