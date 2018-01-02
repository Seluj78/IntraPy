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


class Utils(IntraPy):
    """
        This will be the class for Args
    """

    def __init__(self):
        super().__init__()

    def get_pages(self, url, args):
        result = []
        fixed_parameters = self.get_fixed_parameters(args)
        while args.from_page <= args.to_page:
            response = self.api_get(str(url) + self.get_changeable_parameters(args) + fixed_parameters, "GET")
            ret = json.loads(response.content)
            if not ret:
                break
            i = 0
            while i < len(ret):
                result.append(ret[i])
                i += 1
            args.from_page += 1
        return result

    def get_changeable_parameters(self, args):
        return "?" + "page[number]=" + str(args.from_page)

    def get_fixed_parameters(self, args):
        fixed_parameters = "&page[size]=" + str(args.page_size)
        if type(args.sort) == str:
            fixed_parameters += "&sort=" + str(args.sort)
        if type(args.filter) == str:
            fixed_parameters += "&filter" + str(args.filter)
        #TODO Range
        return fixed_parameters
