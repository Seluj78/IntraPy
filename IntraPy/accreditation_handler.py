import json

from IntraPy import IntraPy


def get_all_accreditations(app_token: str,):
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


def get_accreditation_page(app_token: str, page_number: int):  # TODO: Add page size as variable
    accreditations = []
    response = IntraPy.api_get(app_token, "/v2/accreditations?page[size]=100"
                                          "&page[number]=" + str(page_number),
                               "GET")
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
    print(ret)

# TODO: Add POST PATCH PUT DELETE api endpoint here