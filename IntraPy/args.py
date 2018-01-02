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

import re


class Args:
    """
        This will be the class for Argument handling
        TODO: Extended documentation
        TODO: Better error handling and error messages

        If page_number is explicitely set through options when calling test_get, then the return will be the page PAGE_NUMBER.
        If from_page and to_page are set, it will loop through them
        Else, it will do all the pages until return is empty

    """
    options = {}

    def __init__(self):
        self.page_number = None
        self.page_size = 30
        self.sort = None #TODO: ADD multiple sorts functionality
        self.filter = None #TODO: TEST
        self.range = None # TODO: ADD AND TEST
        self.from_page = None
        self.to_page = None

    def hydrate_values(self, options):
        self.page_number = options.get("page_number", -1)
        if not isinstance(self.page_number, int):
            raise TypeError("page_number must be an int")
        if self.page_number > 0: # ICI, page number a la priorite sur to and from pages
            self.from_page = self.page_number
            self.to_page = self.page_number
        else:
            self.from_page = options.get("from_page", 1)
            if not isinstance(self.from_page, int):
                raise TypeError("from_page must be an int")
            self.to_page = options.get("to_page", 1800)  # 1800 pour 1800 active requests max dans l'api
            if not isinstance(self.to_page, int):
                raise TypeError("to_page must be an int")
        self.page_size = options.get("page_size", 30)
        if not isinstance(self.page_size, int):
            raise TypeError("page_size must be an int")
        elif self.page_size > 100:
            raise ValueError("page_size must be <= 100")
        if self.check_keywords(options) is False:
            return False
        else:
            self.sort = options.get("sort", False)
            self.filter = options.get("filter", False)  # TODO check if works
        self.check_keywords(options)

    def check_keywords(self,options):
        if "rules" not in options: # S'il n'y a pas de regle, l'api de 42 les ignorera =D
            return True
        if "sort" in options and self.sanitize_keyword_string(options.get("sort", "id"),
                                        options["rules"]) is False:
            print("ERROR : Wrong parameters for 'sort' option") # TODO: Error message with wrong parameter
            return False
        if "filter" in options and self.sanitize_keyword_brackets(options.get("filter", "id"),
                                        options["rules"]) is False:
            print("ERROR : Wrong parameters for 'filter' option")
            return False
        return True

    def sanitize_keyword_string(self, string, rules):
        keyword = string.split(',') # cree une liste de chaque mot
        for i, s in enumerate(keyword):
            keyword[i] = re.sub(r'-', '', s) #enleve les '-' avant la comparaison
        return self.compare_with_rules(rules, keyword)

    def sanitize_keyword_brackets(self, string, rules):
        keyword = re.match(r"\[(.*?)\]", string)
        if keyword is None:
            print("ERROR : filter bad format")
            return False
        keyword = keyword.groups()
        return self.compare_with_rules(rules, keyword)

    def compare_with_rules(self, rules, keyword):
        """
        This function will test `keyword` against every entry of the list `rules`.

        :param rules: Rules list containing all authorized rules
        :param keyword: The keyword to test
        :return: If `keyword` isn't found, `False` is returned. `True` otherwise
        """
        for i, s in enumerate(keyword):
            if s not in rules:
                return False
        return True
