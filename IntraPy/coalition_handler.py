import json

from typing import List

from IntraPy import IntraPy

COALITIONS = [
    (0, 'FEDERATION', 'the-federation', 'The Federation'),
    (1, 'ALLIANCE', 'the-alliance', 'The Alliance'),
    (2, 'ASSEMBLY', 'the-assembly', 'The Assembly'),
    (3, 'ORDER', 'the-order', 'The Order')
]


def coalition_get_score(coalition: int, app_token: str) -> int:
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    return ret['coalitions'][coalition]['score']


def coalitions_get_scores(app_token: str) -> List[int]:
    scores = []
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    for coa in COALITIONS:
        scores.append(ret['coalitions'][coa[0]]['score'])
    return scores


def coalition_get_name(coalition: int, app_token: str) -> str:
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    return ret['coalitions'][coalition - 1]['name']


def coalitions_get_names(app_token: str) -> List[str]:
    names = []
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    for coa in COALITIONS:
        names.append(ret['coalitions'][coa[0]]['name'])
    return names


def coalition_get_slug(coalition: int, app_token: str) -> str:
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    return ret['coalitions'][coalition - 1]['slug']


def coalitions_get_slugs(app_token: str) -> List[int]:
    slugs = []
    response = IntraPy.api_get(app_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    for coa in COALITIONS:
        slugs.append(ret['coalitions'][coa[0]]['slug'])
    return slugs