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
        # TODO: Get all the info on the user
        print(ret['login'])
        print(ret['email'])
        print(ret['phone'])
        print(ret['displayname'])
        print(ret['location'])
        print(ret['id'])
        print("coalition={}".format(coalition_id))