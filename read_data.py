import requests
import json
import pandas as pd

URL_GAMES = "https://raw.githubusercontent.com/ropekonsti/konsti/master/server/src/features/statistics/datafiles/ropecon/2022/games.json"
URL_USERS = "https://raw.githubusercontent.com/ropekonsti/konsti/master/server/src/features/statistics/datafiles/ropecon/2022/users.json"
URL_RESULTS = "https://raw.githubusercontent.com/ropekonsti/konsti/master/server/src/features/statistics/datafiles/ropecon/2022/results.json"
URL_SIGNUPS = "https://raw.githubusercontent.com/ropekonsti/konsti/master/server/src/features/statistics/datafiles/ropecon/2022/signups.json"


def read_data(field: str)->pd.DataFrame:
    if (field.upper() == 'RESULTS'):
        data = json.loads(requests.get(URL_RESULTS).text)
        datapd = pd.json_normalize(data, record_path=['results'], meta=['startTime','algorithm','message','updatedAt','createdAt'])
    elif (field.upper() == 'GAMES'):
        data = json.loads(requests.get(URL_GAMES).text)
        datapd = pd.json_normalize(data)
    elif (field.upper() == 'USERS'):
        data = json.loads(requests.get(URL_USERS).text)
        datapd = pd.json_normalize(data, record_path=['signedGames'], meta=['username','userGroup','serial','groupCode','createdAt','updatedAt'])
    elif (field.upper() == 'SIGNUPS'):
        data = json.loads(requests.get(URL_SIGNUPS).text)
        datapd = pd.json_normalize(data, record_path=['userSignups'], meta=[['game','gameId'], 'count','createdAt','updatedAt'])
    else:
        datapd = pd.DataFrame()
    return datapd
