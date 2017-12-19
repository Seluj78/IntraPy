import json

from typing import List

from IntraPy import IntraPy

COALITIONS = [
    (1, 'FEDERATION', 'the-federation', 'The Federation'),
    (2, 'ALLIANCE', 'the-alliance', 'The Alliance'),
    (3, 'ASSEMBLY', 'the-assembly', 'The Assembly'),
    (4, 'ORDER', 'the-order', 'The Order')
]


def coalition_get_score(coalition: int, intrapi_token: str) -> int:
    response = IntraPy.api_get(intrapi_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    return ret['coalitions'][coalition]['score']


def coalitions_get_scores(intrapi_token: str) -> List[int]:
    scores = []
    response = IntraPy.api_get(intrapi_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    for coa in COALITIONS:
        scores.append(ret['coalitions'][coa[0]]['score'])
    return scores


def coalition_get_name(coalition: int, intrapi_token: str) -> str:
    response = IntraPy.api_get(intrapi_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    return ret['coalitions'][coalition - 1]['name']


def coalitions_get_names(intrapi_token: str) -> List[str]:
    names = []
    response = IntraPy.api_get(intrapi_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    for coa in COALITIONS:
        names.append(ret['coalitions'][coa[0]]['name'])
    return names


def coalition_get_slug(coalition: int, intrapi_token: str) -> str:
    response = IntraPy.api_get(intrapi_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    return ret['coalitions'][coalition - 1]['slug']


def coalitions_get_slugs(intrapi_token: str) -> List[int]:
    slugs = []
    response = IntraPy.api_get(intrapi_token, "/v2/blocs/1", "GET")
    ret = json.loads(response.content)
    for coa in COALITIONS:
        slugs.append(ret['coalitions'][coa[0]]['slug'])
    return slugs