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
            raise EnvironmentError("APP_UID wasn't found in your settings.ini file.")
        if APP_SECRET == "None":
            raise EnvironmentError("APP_SECRET wasn't found in your settings.ini file.")
        if TOKEN_FILE == "None":
            raise EnvironmentError("TOKEN_FILE wasn't found in your settings.ini file.")
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

    def api_get(self, uri: str, args, methods="GET"):
        """
        This function will handle all the API requests.
        If the token suddenly expires, this function will call check_token
        and then recursively call itself again until the token works.

        :param args: Arguments passed to the request
        :param uri: The url you want to request from
        :param methods: The method you want to to your API request on. By default, `methods` is set to `GET`

        :return: Returns the response object returned by requests.request()
        """
        result = []
        fixed_parameters = self.get_fixed_parameters(args)
        h = {'Authorization': 'Bearer ' + self.app_token}
        while args.from_page <= args.to_page:
            response = requests.request(methods, "https://api.intra.42.fr" + str(uri) + self.get_changeable_parameters(args) + fixed_parameters, headers=h, allow_redirects=False)
            if response.status_code == 401:
                self.app_token = IntraPy.check_app_token(self)
                return IntraPy.api_get(self, uri, args, methods)
            elif response.status_code == 403:
                time.sleep(int(response.headers["Retry-After"]))
                continue
            ret = json.loads(response.content)
            if not ret:
                break
            i = 0
            while i < len(ret):
                result.append(ret[i])
                i += 1
            args.from_page += 1
        return result

    def api_get_single(self, uri: str, methods="GET"):
        """
        This function will handle all the API requests that send a single json response back.
        If the token suddenly expires, this function will call check_token
        and then recursively call itself again until the token works.

        :param uri: The url you want to request from
        :param methods: The method you want to to your API request on. By default, `methods` is set to `GET`

        :return: Returns the response object returned by requests.request()
        """
        h = {'Authorization': 'Bearer ' + self.app_token}
        response = requests.request(methods, "https://api.intra.42.fr" +
                             uri, headers=h, allow_redirects=False)
        if response.status_code == 401:
            self.app_token = IntraPy.check_app_token(self)
            return IntraPy.api_get_single(self, uri, methods)
        elif response.status_code == 403:
            time.sleep(int(response.headers["Retry-After"]))
            return self.api_get_single(uri, methods)
        return response

    def get_changeable_parameters(self, args):
        """
        This will create and return the string with the parameter that will
        change regularly (the page)

        :param args: The arguments used to get the `from_page` variable

        :return: Returns a string that is appened to the url sent to the api
        """
        return "?" + "page[number]=" + str(args.from_page)

    def get_fixed_parameters(self, args):
        """
        This function will add the strings together to form the part of the url
        where it wont change. This part of the url contains the sorts,
        filters etc...

        :param args: The arguments to add in the url

        :return: Returns a string that is appened to the url sent to the api
        """
        fixed_parameters = "&page[size]=" + str(args.page_size)
        if type(args.sort) == str:
            fixed_parameters += "&sort=" + str(args.sort)
        if type(args.filter) == str:
            fixed_parameters += "&filter" + str(args.filter)
        if type(args.range) == str:
            fixed_parameters += "&range" + str(args.range)
        return fixed_parameters

    def get_uid_from_token(self):
        """
        This function will return the uid of the token from /oauth/token/info

        :return: Returns the uid in a string form
        """
        response = self.api_get_single("/oauth/token/info")
        ret = json.loads(response.content)
        return str(ret["application"]["uid"])

    def get_token_expire_time_in_seconds(self):
        """
        This function will return in how many seconds will the token expire

        :return: Return the time in seconds of when the token will expire
        """
        response = self.api_get_single("/oauth/token/info")
        ret = json.loads(response.content)
        return str(ret["expires_in_seconds"])

    def get_token_expire_time(self):
        """
        This function will return in hours:minutes:seconds the time of expiry of the token

        :return: Returns a string formated in h:m:s
        """
        response = self.api_get_single("/oauth/token/info")
        ret = json.loads(response.content)
        m, s = divmod(ret["expires_in_seconds"], 60)
        h, m = divmod(m, 60)
        return str("%d:%02d:%02d" % (h, m, s))

    def get_token_creation_epoch(self):
        """
        This function will return the epoch time of creation of the token

        :return: Returns a string containing the epoch creation time
        """
        response = self.api_get_single("/oauth/token/info")
        ret = json.loads(response.content)
        return str(ret["created_at"])

    def get_token_creation_date(self):
        """
        This function will return the date and time of creation for the token

        :return: It will return a string in form of `YYYY-MM-DD hh-mm-ss`
        """
        response = self.api_get_single("/oauth/token/info")
        ret = json.loads(response.content)
        return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ret["created_at"])))
