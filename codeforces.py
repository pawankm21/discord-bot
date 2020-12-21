import codeforces_api
# cf_api = codeforces_api.CodeforcesApi(api_key, secret)  #Authorized access.
anonim_cf_api = codeforces_api.CodeforcesApi()  #Unauthorized access.

parser = codeforces_api.CodeforcesParser()  #Parse some info.

contests=codeforces_api.CodeforcesApi().contest_list(gym=False)
