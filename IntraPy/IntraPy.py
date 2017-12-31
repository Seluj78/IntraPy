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
import sys
import requests
from IntraPy.config import APP_UID, APP_SECRET, TOKEN_FILE


class IntraPy:
    """
    This will be the main class for IntraPy
    """

    def __init__(self):
        if APP_UID == "None":
            raise ValueError("APP_UID wasn't found in your settings.ini file.")
        if APP_SECRET == "None":
            raise ValueError("APP_SECRET wasn't found in your settings.ini file.")
        if TOKEN_FILE == "None":
            raise ValueError("TOKEN_FILE wasn't found in your settings.ini file.")
        self.app_secret = APP_SECRET
        self.app_uid = APP_UID
        self.token_file = TOKEN_FILE
        self.app_token = IntraPy.check_app_token(self)

    def api_request_new_token(self):
        d = {'grant_type': 'client_credentials',
             'client_id': self.app_uid, 'client_secret': self.app_secret}
        r = requests.post("https://api.intra.42.fr/oauth/token", data=d)
        print("New access token requested")
        print(r.json()['access_token'])
        with open(self.token_file, "w") as file:
            file.write(r.json()['access_token'])
        return r.json()['access_token']

    def test_token(self):
        self.app_token = IntraPy.get_token_from_file(self)
        h = {'Authorization': 'Bearer ' + self.app_token}
        r = requests.request("GET",
                             "https://api.intra.42.fr" + "/v2/accreditations"
                                                         "?page[size]=1",
                             headers=h, allow_redirects=False)
        try:
            if r.json()['error'] == "Not authorized":
                return False
        except:
            pass
        return True

    def get_token_from_file(self):
        with open(self.token_file, 'r+') as file:
            return file.readline()

    def check_app_token(self):
        if os.path.exists(TOKEN_FILE):
            if os.stat(TOKEN_FILE).st_size != 0:
                if IntraPy.test_token(self):
                    self.app_token = IntraPy.get_token_from_file(self)
                else:
                    self.app_token = IntraPy.api_request_new_token(self)
            else:
                self.app_token = IntraPy.api_request_new_token(self)
        else:
            open(self.token_file, 'a').close()
            self.app_token = IntraPy.api_request_new_token(self)
        with open(self.token_file, "w") as file:
            file.write(str(self.app_token))
        return self.app_token

    def api_get(self, uri: str, methods="GET"):
        h = {'Authorization': 'Bearer ' + self.app_token}
        r = requests.request(methods, "https://api.intra.42.fr" +
                             uri, headers=h, allow_redirects=False)
        try:
            if r.json()['error'] == "Not authorized":
                self.app_token = IntraPy.check_app_token(self)
                return IntraPy.api_get(self, uri, methods)
        except:
            pass
        return r
