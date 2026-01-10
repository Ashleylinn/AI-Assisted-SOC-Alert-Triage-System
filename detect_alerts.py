import csv
from collections import defaultdict

FAILED_LOGIN_THRESHOLD = 5

failed_attempts = defaultdict(int)
user_locations = defaultdict(set)
alerts = []

with open("login_logs.csv", newline="") as file:
    reader = csv.DictReader(file)
    logs = list(reader)

# first pass is success 
for log in logs:
    if log["result"] == "success":
        user_locations[log["user"]].add(log["location"])

# second pass detect suspicious activity 
for log in logs:
    risk = "Low"
    reasons = []

    user = log["user"]

    if log["result"] == "failure":
        failed_attempts[user] += 1
        if failed_attempts[user] >= FAILED_LOGIN_THRESHOLD:
            reasons.append("Multiple failed login attempts")

    if log["location"] not in user_locations[user]:
        reasons.append("Login from unusual location")

    if len(reasons) == 1:
        risk = "Medium"
    elif len(reasons) >= 2:
        risk = "High"

    if risk != "Low":
        alerts.append({
            "timestamp": log["timestamp"],
            "user": user,
            "ip": log["ip"],
            "location": log["location"],
            "risk_level": risk,
            "reasons": reasons
        })

# result
for alert in alerts:
    print(alert)

import json

with open("alerts.json", "w") as f:
    json.dump(alerts, f, indent=2)

print("alerts.json created")