#!/usr/bin/python3

# Phone SMS Sender using python's requests module/library and mailjet api

import requests

# Mailjet API URL
url = "https://api.mailjet.com/v4/sms-send"

# Write the headers
headers = {
        'Authorization': "Bearer b922c6a65470a550d012e72b3d3ca4ec",
        'Content-Type': "application/json"
}

payload = {
        "Text": "Have a nice day!",
        "To": "+919123946055"
}

# Make the post request
response = requests.post(url,headers=headers, data=payload)
print(response.status_code)
