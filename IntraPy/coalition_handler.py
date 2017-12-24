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
from typing import List
from IntraPy import IntraPy


def coalition_get_name(app_token: str, coalition: int) -> str:
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    return ret['coalitions'][coalition - 1]['name']


def coalitions_get_names(app_token: str) -> List[str]:
    names = []
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    coalition_id = 0
    while coalition_id <= 3:
        names.append(ret['coalitions'][coalition_id]['name'])
        coalition_id += 1
    return names


def coalition_get_slug(app_token: str, coalition: int) -> str:
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    return ret['coalitions'][coalition - 1]['slug']


def coalitions_get_slugs(app_token: str) -> List[int]:
    slugs = []
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    coalition_id = 0
    while coalition_id <= 3:
        slugs.append(ret['coalitions'][coalition_id]['slug'])
        coalition_id += 1
    return slugs


def coalition_get_score(app_token: str, coalition: int) -> int:
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    return ret['coalitions'][coalition]['score']


def coalitions_get_scores(app_token: str) -> List[int]:
    scores = []
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    coalition_id = 0
    while coalition_id <= 3:
        scores.append(ret['coalitions'][coalition_id]['score'])
        coalition_id += 1
    return scores
