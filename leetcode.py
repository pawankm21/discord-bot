import requests
import bs4
import json
import random


def randomQuestion():
    r = requests.get(f"https://leetcode.com/api/problems/algorithms/").text

    soup = bs4.BeautifulSoup(r, 'html.parser')
    json_output = json.loads(soup.text)
    problems = []
    for p in json_output['stat_status_pairs']:
        problems.append(p['stat'])

    x = random.randint(0, len(problems)-1)

    return f"https://leetcode.com/problems/{problems[x]['question__title_slug']}"



