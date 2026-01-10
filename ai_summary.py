import json

def generate_summary(alert):
    prompt = f"""
You are a SOC analyst assistant.

Summarize the following security alert in clear, professional language.
Do NOT exaggerate. Be concise.

Alert details:
- User: {alert['user']}
- IP address: {alert['ip']}
- Location: {alert['location']}
- Risk level: {alert['risk_level']}
- Reasons: {', '.join(alert['reasons'])}

Provide:
1. Incident summary
2. Why it may be risky
3. Recommended next action
"""
    return prompt


with open("alerts.json") as f:
    alerts = json.load(f)

for alert in alerts:
    prompt = generate_summary(alert)
    print("\n=== AI PROMPT ===")
    print(prompt)
