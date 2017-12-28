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
from IntraPy.IntraPy import IntraPy


class Test(IntraPy):
    def __init__(self):
        super().__init__()

    def get_options(self, options):
        #TODO gestion des flags pour filter, sort et range. Param global ?
        str_options = "?" + \
                      "page[size]=" + str(options.get("page_size", 30))\
                      + "&"\
                      + "page[number]=" + str(options.get("page_index", 1))\
                      + "&"\
                     # + "" if not options.has_key("sort") else "sort=" + options.get("sort", "id")
        return str_options

    def get_test(self, test_url: str, options=None, pretty = False):
        if options is None:
            options = {}
        achievements = []
        options["page_index"] = 1

        if options.get("page_size", 30) > 100:
            options["page_size"] = 100 #TODO return an error

        while options["page_index"] <= options.get("page_number", 1):
            response = self.api_get("/v2/" + str(test_url)
                                    + self.get_options(options)
                                    , "GET")
            ret= json.loads(response.content)
            i = 0
            while i < len(ret):
                achievements.append(ret[i])
                i += 1
            options["page_index"] += 1

        if pretty:
            return json.dumps(achievements, indent=4, sort_keys=True)
        return achievements