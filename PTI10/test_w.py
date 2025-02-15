import json
data = [{"name": "Bob", "age": 28, "city": "Paris"}, {"name": "Bob", "age": 28, "city": "Paris"}]

with open('App Mixue/db/account.json', 'w') as file:
    json.dump(data, file, indent=4)

