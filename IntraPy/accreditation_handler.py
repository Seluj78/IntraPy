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


def get_all_accreditations(app_token: str):
    accreditations = []
    page_number = 1
    while page_number <= 10:  # Warning: This number needs to be changed if
        # the number of accreditations given gets bigger than 100 * 10
        response = IntraPy.api_get(app_token, "/v2/accreditations?page[size]=100"
                                              "&page[number]=" +
                                   str(page_number), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            accreditations.append(ret[i])
            i += 1
        page_number = page_number + 1
    return accreditations


def get_accreditation_page_number_and_size(app_token: str, page_number: int, page_size: int):
    accreditations = []
    response = IntraPy.api_get(app_token, "/v2/accreditations?page[size]=" + str(page_size) + "&page[number]=" + str(page_number), "GET")
    ret = json.loads(response.content)
    i = 0
    while i < len(ret):
        accreditations.append(ret[i])
        i += 1
    return accreditations


def get_accreditation_by_id(app_token: str, accreditation_id: int):
    response = IntraPy.api_get(app_token, "/v2/accreditations/" +
                               str(accreditation_id), "GET")
    ret = json.loads(response.content)
    return ret
