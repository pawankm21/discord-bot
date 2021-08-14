import requests
from bs4 import BeautifulSoup
import codeforces_api


def future_contests():
  url = "https://www.codechef.com/contests"

  r = requests.get(url).text
  soup = BeautifulSoup(r, 'lxml')
  contest = []
  soup.find_all("div", {"id": "futer-contest-data"})
  print(contest)
  return contest


anonim_cf_api = codeforces_api.CodeforcesApi()
codeforces_contests = anonim_cf_api.contest_list()['result']
