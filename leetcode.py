import requests
import bs4
import json
import random

class Leetcode:
    r = requests.get(f"https://leetcode.com/api/problems/algorithms/").text
    soup = bs4.BeautifulSoup(r, 'html.parser')
    json_output = json.loads(soup.text)
    questions=json_output['stat_status_pairs']
    def randomQuestion(self):
        problems = []
        for question in self.questions:
            problems.append(question['stat'])

        x = random.randint(0, len(problems)-1)

        return f"https://leetcode.com/problems/{problems[x]['question__title_slug']}"

    def getByName(self,name,maxoutput=1):
        list_of_questions=[]
        terms=list(name.split('-'))
        for question in self.questions:
            for term in terms:
                if term in question['stat']['question__title']:
                    list_of_questions.append(
                        f"https://leetcode.com/problems/{question['stat']['question__title_slug']}")
            random.shuffle(list_of_questions)
        return list_of_questions[:maxoutput]



v=Leetcode()
print(v.getByName('BST'))
