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


class AchievementById(IntraPy):
    def __init__(self):
        super().__init__()

    def get_achievement_by_id(self, achievement_id: int):
        response = IntraPy.IntraPy.api_get(self, "/v2/achievements/" +
                                           str(achievement_id), "GET")
        ret = json.loads(response.content)
        return ret
