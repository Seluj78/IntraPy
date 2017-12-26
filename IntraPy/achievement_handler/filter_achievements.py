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

import json
from IntraPy import IntraPy


def get_all_achievements_with_filter(app_token: str, filter_name: str, value: str):
    achievements = []
    page_number = 1
    available_filters = ["id", "name", "internal_name", "kind", "tier",
                         "description", "pedago", "visible", "nbr_of_success",
                         "parent_id", "image", "created_at", "updated_at",
                         "slug", "position", "reward", "title_id"]
    if filter_name not in available_filters:
        print("Error: the `filter' parameter given to "
              "get_all_achievements_sorted isn't recognised")
        return
    while page_number <= 3:  # TODO: Warning: This number might need to change
        response = IntraPy.api_get(app_token, "/v2/achievements?page[size]=100&"
                                              "page[number]=" + str(page_number)
                                   + "&filter[" + str(filter_name) + "]="
                                   + str(value), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_all_achievements_with_filter_cursus(app_token: str, filter_name: str, value: str, cursus_id: int):
    achievements = []
    page_number = 1
    available_filters = ["id", "name", "internal_name", "kind", "tier",
                         "description", "pedago", "visible", "nbr_of_success",
                         "parent_id", "image", "created_at", "updated_at",
                         "slug", "position", "reward", "title_id"]
    if filter_name not in available_filters:
        print("Error: the `filter' parameter given to "
              "get_all_achievements_sorted isn't recognised")
        return
    while page_number <= 3:  # TODO: Warning: This number might need to change
        response = IntraPy.api_get(app_token, "/v2/cursus/" + str(cursus_id)
                                   + "/achievements?page[size]=100"
                                     "&page[number]=" + str(page_number)
                                   + "&filter[" + str(filter_name) + "]="
                                   + str(value), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_all_achievements_with_filter_campus(app_token: str, filter_name: str, value: str, campus_id: int):
    achievements = []
    page_number = 1
    available_filters = ["id", "name", "internal_name", "kind", "tier",
                         "description", "pedago", "visible", "nbr_of_success",
                         "parent_id", "image", "created_at", "updated_at",
                         "slug", "position", "reward", "title_id"]
    if filter_name not in available_filters:
        print("Error: the `filter' parameter given to "
              "get_all_achievements_sorted isn't recognised")
        return
    while page_number <= 3:  # TODO: Warning: This number might need to change
        response = IntraPy.api_get(app_token, "/v2/campus/" + str(campus_id)
                                   + "/achievements?page[size]=100"
                                     "&page[number]=" + str(page_number)
                                   + "&filter[" + str(filter_name) + "]="
                                   + str(value), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements
