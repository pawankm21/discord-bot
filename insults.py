import requests
import json
url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
r=requests.get(url)
insults_json=r.json()
print(insults_json['insult'])
