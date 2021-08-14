from youtubesearchpython import VideosSearch
from pytube import YouTube


def yts(srch, limit):

    videosSearch = VideosSearch(srch, limit=limit)
    temp = []
    for i in range(limit):
        temp.append(videosSearch.result()['result'][i]['link'])
    return temp
