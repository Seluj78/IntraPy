"""
    A python Library to help make python apps/bots using the 42 API
    Copyright (C) 2017-2018  Jules LASNE jlasne@student.42.fr

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import requests
from typing import Union
from IntraPy.config import APP_UID, APP_SECRET, TOKEN_FILE


def api_request_new_token(uid: str, secret: str) -> str:
    d = {'grant_type': 'client_credentials',
         'client_id': uid, 'client_secret': secret}
    r = requests.post("https://api.intra.42.fr/oauth/token", data=d)
    print("New access token requested")
    print(r.json()['access_token'])
    with open(TOKEN_FILE, "w") as file:
        file.write(r.json()['access_token'])
    return r.json()['access_token']


def api_get(app_token: Union[str, None], uri: str, methods="GET"):
    h = {'Authorization': 'Bearer ' + app_token}
    r = requests.request(methods, "https://api.intra.42.fr" +
                         uri, headers=h, allow_redirects=False)
    try:
        if r.json()['error'] == "Not authorized":
            app_token = check_app_token()
            return api_get(app_token, uri, methods)
    except:
        pass
    return r


def test_token():
    with open(TOKEN_FILE, 'r') as file:
        app_token = file.readline()
    h = {'Authorization': 'Bearer ' + app_token}
    r = requests.request("GET", "https://api.intra.42.fr" + "/v2/accreditations"
                                                            "?page[size]=1",
                         headers=h,allow_redirects=False)
    try:
        if r.json()['error'] == "Not authorized":
            return False
    except:
        pass
    return True


def get_token_from_file():
    with open(TOKEN_FILE, 'r+') as file:
        return file.readline()


def check_app_token():
    if os.path.exists(TOKEN_FILE):
        if os.stat(TOKEN_FILE).st_size != 0:
            if test_token():
                app_token = get_token_from_file()
            else:
                app_token = api_request_new_token(APP_UID, APP_SECRET)
        else:
            app_token = api_request_new_token(APP_UID, APP_SECRET)
    else:
        open(TOKEN_FILE, 'a').close()
        app_token = api_request_new_token(APP_UID, APP_SECRET)
    with open(TOKEN_FILE, "w") as file:
        file.write(str(app_token))
    return app_token


def init() -> str:
    if not (APP_SECRET and APP_UID and TOKEN_FILE):
        print("42\'s variables (App secret, App UID, and the token file or "
              "both) are not set either in your environment variables or in "
              "the settings.ini file.")
        exit(EnvironmentError)
    return check_app_token()
