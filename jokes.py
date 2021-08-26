import requests


def jokes(query):
  query.capitalize()
  url = f"https://v2.jokeapi.dev/joke/Any?type=single"
  r = requests.get(url)
  joke_json = r.json()
  return joke_json
