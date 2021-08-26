import requests
from bs4 import BeautifulSoup
import codeforces_api


def future_contests():

    url = "https://www.codechef.com/contests/?itm_medium=navmenu&itm_campaign=allcontests_head"

    payload = {}
    headers = {
        'Cookie': 'SESS93b6022d778ee317bf48f7dbffe03173=d9752da233ebc9cef84d7b1de79d7407'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    soup = BeautifulSoup(response, 'lxml')
    contest = soup.find("li",)

    return contest


anonim_cf_api = codeforces_api.CodeforcesApi()
codeforces_contests = anonim_cf_api.contest_list()['result']
