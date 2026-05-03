import urllib.request
import json

url = "https://api.nodemailer.com/user"
req = urllib.request.Request(url, data=json.dumps({"requestor": "SmartCivicApp"}).encode('utf-8'), headers={'Content-Type': 'application/json'}, method='POST')

try:
    with urllib.request.urlopen(req) as response:
        account = json.loads(response.read().decode('utf-8'))
        print("--- ETHEREAL SMTP CREDENTIALS ---")
        print(f"HOST: {account['smtp']['host']}")
        print(f"PORT: {account['smtp']['port']}")
        print(f"USER: {account['user']}")
        print(f"PASS: {account['pass']}")
        print(f"INBOX: https://ethereal.email/messages")
except Exception as e:
    print(f"Failed: {e}")
