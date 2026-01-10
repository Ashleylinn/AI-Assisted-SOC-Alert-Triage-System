import json

def ai_summary(alert):
    """
    Simulated AI-assisted incident summary.
    (In real deployment, this would call an LLM API.)
    """
    summary = (
        f"Multiple authentication anomalies were detected for user "
        f"{alert['user']} from IP address {alert['ip']}."
    )

    risk_explanation = (
        "The activity includes repeated failed login attempts and "
        "access from an unfamiliar geographic location."
        if alert["risk_level"] == "High"
        else "The activity deviates from the user's normal login behavior."
    )

    recommended_action = (
        "Lock the account temporarily and investigate the source IP."
        if alert["risk_level"] == "High"
        else "Monitor the account for further suspicious activity."
    )

    return {
        "incident_summary": summary,
        "risk_explanation": risk_explanation,
        "recommended_action": recommended_action
    }


with open("alerts.json") as f:
    alerts = json.load(f)

incident_reports = []

for alert in alerts:
    ai_output = ai_summary(alert)

    incident_reports.append({
        "timestamp": alert["timestamp"],
        "user": alert["user"],
        "ip": alert["ip"],
        "location": alert["location"],
        "risk_level": alert["risk_level"],
        "reasons": alert["reasons"],
        "ai_summary": ai_output
    })

with open("incident_reports.json", "w") as f:
    json.dump(incident_reports, f, indent=2)

print("incident_reports.json created")
