import requests
import json
url = "https://smalltalk-nlu.p.rapidapi.com/api/v1/smalltalk"

payload = "languageCode=en-US&query=hola"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "b53a7afe17mshee0ecf8b2fcc4e6p1f2631jsn2d48c750102a",
    'x-rapidapi-host': "smalltalk-nlu.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)
talkback=response.json()
# intent = json.dumps(talkback['intent'])
# talkback=json.dumps(talkback['fulfillmentMessages']['text'][0])
print(response.text)
