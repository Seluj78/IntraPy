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
import json
import time
import requests
from IntraPy.config import APP_UID, APP_SECRET, TOKEN_FILE


class IntraPy:
    """
        This is the main class for IntraPy. It contains the app_token handling
        and any other widely used function throughout the module as IntraPy
        expands many classes
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
        """
        This function will request a new token to the 42 api

        :return: Returns the newly requested token
        """
        d = {'grant_type': 'client_credentials',
             'client_id': self.app_uid, 'client_secret': self.app_secret}
        r = requests.post("https://api.intra.42.fr/oauth/token", data=d)
        print("New access token requested")
        print(r.json()['access_token'])
        with open(self.token_file, "w") as file:
            file.write(r.json()['access_token'])
        return r.json()['access_token']

    def test_token(self):
        """
        This function will test on `/oauth/token/info` if the token is still
        available and hasn't expired

        :return: Returns True if the token is still usable, False otherwise.
        """
        self.app_token = IntraPy.get_token_from_file(self)
        h = {'Authorization': 'Bearer ' + self.app_token}
        r = requests.request("GET",
                             "https://api.intra.42.fr" + "/oauth/token/info", headers=h, allow_redirects=False)
        try:
            if r.json()['error'] == "invalid_request":
                return False
        except:
            pass
        return True

    def get_token_from_file(self):
        """
        This function will get from the TOKEN_FILE file the first line
        :return: Returns the first line of the token file containing the
        app token.
        """
        with open(self.token_file, 'r+') as file:
            return file.readline()

    def check_app_token(self):
        """
        This function will check every possible case of error possible with
        the app token:
        If the file doesn't exists
        If the file is empty
        If the token is expired/incomplete

        :return: Returns the app_token string
        """
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
        """
        This function will handle all the API requests.
        If the token suddenly expires, this function will call check_token
        and then recursively call itself again until the token works.

        :param uri: The url you want to request from
        :param methods: The method you want to to your API request on. By default, `methods` is set to `GET`

        :return: Returns the response object returned by requests.request()
        """
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

    def get_uid_from_token(self):
        response = self.api_get("/oauth/token/info")
        ret = json.loads(response.content)
        return ret["application"]["uid"]

    def get_token_expire_time_in_seconds(self):
        response = self.api_get("/oauth/token/info")
        ret = json.loads(response.content)
        return ret["expires_in_seconds"]

    def get_token_expire_time(self):
        response = self.api_get("/oauth/token/info")
        ret = json.loads(response.content)
        m, s = divmod(ret["expires_in_seconds"], 60)
        h, m = divmod(m, 60)
        return "%d:%02d:%02d" % (h, m, s)

    def get_token_creation_epoch(self):
        response = self.api_get("/oauth/token/info")
        ret = json.loads(response.content)
        return ret["created_at"]

    def get_token_creation_date(self):
        response = self.api_get("/oauth/token/info")
        ret = json.loads(response.content)
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ret["created_at"]))
