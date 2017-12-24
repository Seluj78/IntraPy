'''
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
'''

import json
from IntraPy import IntraPy


def coalition_update_local_list(coalition_id: int, app_token: str,):
    users = []
    page_number = 1
    while page_number <= 10:
        response = IntraPy.api_get(app_token, "/v2/coalitions/" + str(coalition_id) + "/coalitions_users?page[size]=100&page[number]=" + str(page_number), "GET")
        ret = json.loads(response.content)
        for item in ret:
            users.append(item.get('user_id'))
        page_number = page_number + 1
    for user in users:
        response = IntraPy.api_get(app_token, "/v2/users/{}".format(user), "GET")
        ret = json.loads(response.content)
        print(ret['login'])
        print(ret['email'])
        print(ret['phone'])
        print(ret['displayname'])
        print(ret['location'])
        print(ret['id'])
        print("coalition={}".format(coalition_id))