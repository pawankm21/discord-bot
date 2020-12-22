import codeforces_api
# cf_api = codeforces_api.CodeforcesApi(api_key, secret)  #Authorized access.
anonim_cf_api = codeforces_api.CodeforcesApi()  #Unauthorized access.

parser = codeforces_api.CodeforcesParser()  #Parse some info.

api_result=codeforces_api.CodeforcesApi().contest_list(gym=False)
contests_codeforces =[]
contest_id =[]
i=0
for contest in api_result['result']:
    if contest['phase']!='FINISHED':
        contests_codeforces.append(contest['name'])
        contest_id.append(contest['id'])
