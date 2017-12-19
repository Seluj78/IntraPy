from typing import Union

import requests

from IntraPy.config import APP_UID, APP_SECRET


def api_request_new_token(uid: str, secret: str) -> str:
    d = {'grant_type': 'client_credentials',
         'client_id': uid, 'client_secret': secret}
    r = requests.post("https://api.intra.42.fr/oauth/token", data=d)
    print("New access token requested")
    print(r.json()['access_token'])
    with open(".app_token", "w") as file:
        file.write(r.json()['access_token'])
    return r.json()['access_token']


def api_get(key: Union[str, None], uri: str, methods="GET"):
    h = {'Authorization': 'Bearer ' + key}
    r = requests.request(methods, "https://api.intra.42.fr" +
                         uri, headers=h, allow_redirects=False)
    try:
        if r.json()['error'] == "Not authorized":
            print("Warning: Key expired or not authorized.")
            print("Trying requesting a new token.")
            key = api_request_new_token(APP_UID, APP_SECRET).json()['access_token']
            print("Received new access token.")
            return api_get(uri, methods)
    except:
        pass
    return r


def init() -> Union[str, None]:
    if not (APP_SECRET and APP_UID):
        print('42\'s variables (App secret, App UID, or both) are'
              ' not set either in your environment variables or in the settings.ini file.')
        return None
    try:
        with open('.app_token', 'r+') as file:
            key = file.readline()
    except FileNotFoundError:
        key = None
        print('The file .app_token wasnt found. We created it and populated it')
        open('.app_token', 'a').close()
    if not key:
        key = api_request_new_token(APP_UID, APP_SECRET)
        return key
    else:
        return key
