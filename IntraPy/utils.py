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

    def get_all_pages(self, str_url, arg):
        achievements = []
        optionnal = self.get_optionnal(arg) #pour eviter de refaire une string qui ne changera jamais
        while arg.page_index <= arg.page_number:
            response = self.api_get(str(str_url)
                                    + self.get_changeable(arg)
                                    + optionnal
                                    , "GET")
            ret = json.loads(response.content)
            i = 0
            while i < len(ret):
                achievements.append(ret[i])
                i += 1
            arg.page_index += 1
        return achievements

    def get_changeable(self, arg):
        number = "page[number]=" + str(arg.page_index)
        str_options = "?" + number
        return str_options

    def get_optionnal(self, arg):
        optionnal = "&page[size]=" + str(arg.page_size)
        if type(arg.sort) == str:
            optionnal += "&sort=" + str(arg.sort)
        if type(arg.filter) == str:
            optionnal += "&filter" + str(arg.filter)
        #TODO Range
        return optionnal