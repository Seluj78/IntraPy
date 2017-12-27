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
from typing import List
from IntraPy import IntraPy
from IntraPy.IntraPy import IntraPy


class Coalitions(IntraPy):
    def __init__(self):
        super().__init__()

    def coalition_get_name(self, coalition: int) -> str:
        response = IntraPy.IntraPy.api_get(self, "/v2/blocs/1", "GET")
        ret = json.loads(response.content)
        return ret['coalitions'][coalition - 1]['name']

    def coalitions_get_names(self) -> List[str]:
        names = []
        response = IntraPy.IntraPy.api_get(self, "/v2/blocs/1", "GET")
        ret = json.loads(response.content)
        coalition_id = 0
        while coalition_id <= 3:
            names.append(ret['coalitions'][coalition_id]['name'])
            coalition_id += 1
        return names

    def coalition_get_slug(self, coalition: int) -> str:
        response = IntraPy.IntraPy.api_get(self, "/v2/blocs/1", "GET")
        ret = json.loads(response.content)
        return ret['coalitions'][coalition - 1]['slug']

    def coalitions_get_slugs(self) -> List[int]:
        slugs = []
        response = IntraPy.IntraPy.api_get(self, "/v2/blocs/1", "GET")
        ret = json.loads(response.content)
        coalition_id = 0
        while coalition_id <= 3:
            slugs.append(ret['coalitions'][coalition_id]['slug'])
            coalition_id += 1
        return slugs

    def coalition_get_score(self, coalition: int) -> int:
        response = IntraPy.IntraPy.api_get(self, "/v2/blocs/1", "GET")
        ret = json.loads(response.content)
        return ret['coalitions'][coalition]['score']

    def coalitions_get_scores(self) -> List[int]:
        scores = []
        response = IntraPy.IntraPy.api_get(self, "/v2/blocs/1", "GET")
        ret = json.loads(response.content)
        coalition_id = 0
        while coalition_id <= 3:
            scores.append(ret['coalitions'][coalition_id]['score'])
            coalition_id += 1
        return scores
