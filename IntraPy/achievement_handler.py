import json
from IntraPy import IntraPy


def get_all_achievements(app_token: str):
    achievements = []
    page_number = 1
    while page_number <= 3:  # TODO: Change this matching to the number of
                                                    # achievements availables
        response = IntraPy.api_get(app_token, "/v2/achievements?page[size]=100"
                                              "&page[number]=" +
                                   str(page_number), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_all_achievements_with_sort(app_token: str, sort: str):
    achievements = []
    page_number = 1
    available_sorts = ["id", "name", "internal_name", "kind", "tier",
                       "description", "pedago", "visible", "nbr_of_success",
                       "parent_id", "image", "created_at", "updated_at", "slug",
                       "position", "reward", "title_id"]
    if sort not in available_sorts:
        print("Error: the `sort' parameter given to get_all_achievements_sorted"
              " isn't recognised")
        return
    while page_number <= 3:  # TODO: Warning: This number might need to change
        response = IntraPy.api_get(app_token, "/v2/achievements?page[size]=100&"
                                              "page[number]=" + str(page_number)
                                   + "&sort=" + str(sort), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_all_achievements_with_filter(app_token: str, filter: str, value: str):
    achievements = []
    page_number = 1
    available_filters = ["id", "name", "internal_name", "kind", "tier",
                         "description", "pedago", "visible", "nbr_of_success",
                         "parent_id", "image", "created_at", "updated_at",
                         "slug", "position", "reward", "title_id"]
    if filter not in available_filters:
        print("Error: the `filter' parameter given to "
              "get_all_achievements_sorted isn't recognised")
        return
    while page_number <= 3:  # TODO: Warning: This number might need to change
        response = IntraPy.api_get(app_token, "/v2/achievements?page[size]=100&"
                                              "page[number]=" + str(page_number)
                                   + "&filter[" + str(filter) + "]="
                                   + str(value), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_achievements_page_number_and_size(app_token: str, page_number: int, page_size: int):
    achievements = []
    response = IntraPy.api_get(app_token, "/v2/achievements?page[size]="
                               + str(page_size) + "&page[number]="
                               + str(page_number), "GET")
    ret = json.loads(response.content)
    i = 0
    while i < len(ret):
        achievements.append(ret[i])
        i += 1
    return achievements


def get_achievement_by_id(app_token: str, achievement_id: int):
    response = IntraPy.api_get(app_token, "/v2/achievements/" +
                               str(achievement_id), "GET")
    ret = json.loads(response.content)
    return ret


def get_all_achievements_cursus(app_token: str, cursus_id: int):
    achievements = []
    page_number = 1
    while page_number <= 3:  # TODO: Change this matching to the number of
                                                    # achievements availables
        response = IntraPy.api_get(app_token, "/v2/cursus/" + str(cursus_id)
                                   + "/achievements?page[size]=100"
                                     "&page[number]=" + str(page_number), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_all_achievements_with_sort_cursus(app_token: str, sort: str, cursus_id: int):
    achievements = []
    page_number = 1
    available_sorts = ["id", "name", "internal_name", "kind", "tier",
                       "description", "pedago", "visible", "nbr_of_success",
                       "parent_id", "image", "created_at", "updated_at", "slug",
                       "position", "reward", "title_id"]
    if sort not in available_sorts:
        print("Error: the `sort' parameter given to get_all_achievements_sorted"
              " isn't recognised")
        return
    while page_number <= 3:  # TODO: Warning: This number might need to change
        response = IntraPy.api_get(app_token, "/v2/cursus/" + str(cursus_id)
                                   + "/achievements?page[size]=100"
                                     "&page[number]=" + str(page_number)
                                   + "&sort=" + str(sort), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_all_achievements_with_filter_cursus(app_token: str, filter: str, value: str, cursus_id: int):
    achievements = []
    page_number = 1
    available_filters = ["id", "name", "internal_name", "kind", "tier",
                         "description", "pedago", "visible", "nbr_of_success",
                         "parent_id", "image", "created_at", "updated_at",
                         "slug", "position", "reward", "title_id"]
    if filter not in available_filters:
        print("Error: the `filter' parameter given to "
              "get_all_achievements_sorted isn't recognised")
        return
    while page_number <= 3:  # TODO: Warning: This number might need to change
        response = IntraPy.api_get(app_token, "/v2/cursus/" + str(cursus_id)
                                   + "/achievements?page[size]=100"
                                     "&page[number]=" + str(page_number)
                                   + "&filter[" + str(filter) + "]="
                                   + str(value), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_achievements_page_number_and_size_cursus(app_token: str, page_number: int, page_size: int, cursus_id: int):
    achievements = []
    response = IntraPy.api_get(app_token, "/v2/cursus/" + str(cursus_id)
                               + "/achievements?page[size]=" + str(page_size)
                               + "&page[number]=" + str(page_number), "GET")
    ret = json.loads(response.content)
    i = 0
    while i < len(ret):
        achievements.append(ret[i])
        i += 1
    return achievements

def get_all_achievements_campus(app_token: str, campus_id: int):
    achievements = []
    page_number = 1
    while page_number <= 3:  # TODO: Change this matching to the number of
                                                    # achievements availables
        response = IntraPy.api_get(app_token, "/v2/campus/" + str(campus_id)
                                   + "/achievements?page[size]=100"
                                     "&page[number]=" + str(page_number), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_all_achievements_with_sort_campus(app_token: str, sort: str, campus_id: int):
    achievements = []
    page_number = 1
    available_sorts = ["id", "name", "internal_name", "kind", "tier",
                       "description", "pedago", "visible", "nbr_of_success",
                       "parent_id", "image", "created_at", "updated_at", "slug",
                       "position", "reward", "title_id"]
    if sort not in available_sorts:
        print("Error: the `sort' parameter given to get_all_achievements_sorted"
              " isn't recognised")
        return
    while page_number <= 3:  # TODO: Warning: This number might need to change
        response = IntraPy.api_get(app_token, "/v2/campus/" + str(campus_id)
                                   + "/achievements?page[size]=100"
                                     "&page[number]=" + str(page_number)
                                   + "&sort=" + str(sort), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_all_achievements_with_filter_campus(app_token: str, filter: str, value: str, campus_id: int):
    achievements = []
    page_number = 1
    available_filters = ["id", "name", "internal_name", "kind", "tier",
                         "description", "pedago", "visible", "nbr_of_success",
                         "parent_id", "image", "created_at", "updated_at",
                         "slug", "position", "reward", "title_id"]
    if filter not in available_filters:
        print("Error: the `filter' parameter given to "
              "get_all_achievements_sorted isn't recognised")
        return
    while page_number <= 3:  # TODO: Warning: This number might need to change
        response = IntraPy.api_get(app_token, "/v2/campus/" + str(campus_id)
                                   + "/achievements?page[size]=100"
                                     "&page[number]=" + str(page_number)
                                   + "&filter[" + str(filter) + "]="
                                   + str(value), "GET")
        ret = json.loads(response.content)
        i = 0
        while i < len(ret):
            achievements.append(ret[i])
            i += 1
        page_number = page_number + 1
    return achievements


def get_achievements_page_number_and_size_campus(app_token: str, page_number: int, page_size: int, campus_id: int):
    achievements = []
    response = IntraPy.api_get(app_token, "/v2/campus/" + str(campus_id)
                               + "/achievements?page[size]=" + str(page_size)
                               + "&page[number]=" + str(page_number), "GET")
    ret = json.loads(response.content)
    i = 0
    while i < len(ret):
        achievements.append(ret[i])
        i += 1
    return achievements


# TODO: Multiple sorts, filter and ranges
# TODO: get_achievements_page_number_and_size with filter, sort, ranges
# TODO: GET /v2/titles/:title_id/achievements
