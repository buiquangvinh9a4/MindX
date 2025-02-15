import json


with open('App Mixue/db/account.json', 'r') as file:
    data = json.load(file)
    print(data)
