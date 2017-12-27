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
from IntraPy.IntraPy import IntraPy


class GetAllAchievements(IntraPy):
    def __init__(self):
        super().__init__()

    def get_all_achievements(self):
        achievements = []
        page_number = 1
        while page_number <= 3:  # TODO: Change this matching to the number of
            # achievements availables
            response = IntraPy.IntraPy.api_get(self,
                                       "/v2/achievements?page[size]=100"
                                       "&page[number]=" +
                                       str(page_number), "GET")
            ret = json.loads(response.content)
            i = 0
            while i < len(ret):
                achievements.append(ret[i])
                i += 1
            page_number = page_number + 1
        return achievements

    def get_all_achievements_cursus(self, cursus_id: int):
        achievements = []
        page_number = 1
        while page_number <= 3:  # TODO: Change this matching to the number of
            # achievements availables
            response = IntraPy.IntraPy.api_get(self, "/v2/cursus/" + str(cursus_id)
                                       + "/achievements?page[size]=100"
                                         "&page[number]=" + str(page_number),
                                       "GET")
            ret = json.loads(response.content)
            i = 0
            while i < len(ret):
                achievements.append(ret[i])
                i += 1
            page_number = page_number + 1
        return achievements

    def get_all_achievements_campus(self, campus_id: int):
        achievements = []
        page_number = 1
        while page_number <= 3:  # TODO: Change this matching to the number of
            # achievements availables
            response = IntraPy.IntraPy.api_get(self, "/v2/campus/" + str(campus_id)
                                       + "/achievements?page[size]=100"
                                         "&page[number]=" + str(page_number),
                                       "GET")
            ret = json.loads(response.content)
            i = 0
            while i < len(ret):
                achievements.append(ret[i])
                i += 1
            page_number = page_number + 1
        return achievements
