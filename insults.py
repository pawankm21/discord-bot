import requests
def insults():
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    r = requests.get(url)
    insults_json = r.json()
    return insults_json;

