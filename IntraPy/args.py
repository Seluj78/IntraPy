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
        This class here handles the arguments.
        TODO: Better error handling and error messages
    """


    """
        @todo Add option priority explaination in the wiki
        @body If page_number is explicitely set through options when calling test_get, then the return will be the page PAGE_NUMBER. If from_page and to_page are set, it will loop through them Else, it will do all the pages until return is empty. priority on page_number. 1800 requetes max pour to_page car 1800 requete en limite de l'api. a tester
    """

    options = {}

    def __init__(self):
        """
        Here, we define default value for each variable that can be passed
        to the kwargs
        """
        self.page_number = None
        self.page_size = 30
        self.sort = None
        self.filter = None
        self.range = None
        self.from_page = None
        self.to_page = None
        self.pretty = False

    def hydrate_values(self, options):
        """
        This function will get from the options passed their values, and if
        they aren't correct, it will throw an error

        :param options: The options passed
        :return: Returns False if an error occurs
        """
        self.page_number = options.get("page_number", -1)
        if not isinstance(self.page_number, int):
            raise TypeError("page_number must be an int")
        if self.page_number > 0:
            self.from_page = self.page_number
            self.to_page = self.page_number
        else:
            self.from_page = options.get("from_page", 1)
            if not isinstance(self.from_page, int):
                raise TypeError("from_page must be an int")
            """
            @todo Test 1800 limit for to_page
            @body the `to_page` variable has a 1800 limit set because of the api limtation. it needs to be correctly tested.
            """
            self.to_page = options.get("to_page", 1800)
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
            self.filter = options.get("filter", False)
            self.range = options.get("range", False)
        self.check_keywords(options)

    def check_keywords(self, options):
        """
        This function will check if the keywords given to `filter` and `sort`
        are in the ruleset.

        :param options: The options passed
        :return: Returns False is any keyword isn't in the authorized rules
        """
        if "rules" not in options:
            return True
        if "sort" in options and self.sanitize_keyword_string(options.get("sort", "id"), options["rules"]) is False:
            raise ValueError("Wrong value for `sort` parameter: '" + options.get("sort", "id") + "'")
        if "filter" in options and self.sanitize_keyword_brackets(options.get("filter", "id"), options["rules"]) is False:
            raise ValueError("Wrong value for `filter` parameter: '" + options.get("filter", "id") + "'")
        if "range" in options and self.sanitize_keyword_range(options.get("range", "id"), options["rules"]) is False:
            """
            @todo Shorten error messages
            """
            raise ValueError("Wrong value for `range` parameter: '" + options.get("range", "id")[options.get("range", "id").find("[") + 1:options.get("range", "id").find("]")] + "'")
        return True

    def sanitize_keyword_string(self, string, rules):
        """
        This function will split the `sort` string `string` into keyword and
        compare each one to the given rules.

        :param string: The string to split into keywords
        :param rules: The rules authorized
        :return: Returns `False` if the sort options aren't in rules
        """

        """
            @todo Add multiple sorts
            @body Multiple sort parameters isn't handled, eg. `sort="one"&sort="two"`
        """

        if not isinstance(string, str):
            raise ValueError("sort must be a String")
        keyword = string.split(',')
        for i, s in enumerate(keyword):
            keyword[i] = re.sub(r'-', '', s)
        return self.compare_with_rules(rules, keyword)

    def sanitize_keyword_brackets(self, string, rules):
        """
        This function will split the `filter` string `string` into keyword and
        compare each one to the given rules.

        :param string: The string to split into keywords
        :param rules: The rules authorized
        :return: Returns `False` if the filter options aren't in rules
        """

        filter_asked = string[string.find("[") + 1:string.find("]")]
        if filter_asked not in rules:
            return False
        filters = string.split("=")[1]
        if self.are_ranges_ints(filters):
            return True
        else:
            raise ValueError("Error: One parameter for range isn't an string or it isn't in the rules")

    def sanitize_keyword_range(self, string, rules):
        """
        This will check that the range option works correctly, and that the
        values passed are correct and ints
        Here, we aren't calling compare_with_rules because range doesn't get keywords but values

        :param string: The string containing the options for range
        :param rules: The ruleset

        :return: Returns True if everything is ok, False otherwise
        """
        range_asked = string[string.find("[") + 1:string.find("]")]
        if range_asked not in rules:
            return False
        second = string.split(",")[1]
        first = string.split(",")[0].split("=")[1]
        if not self.is_an_int(first):
            raise ValueError("Error: First parameter for range parameter isn't an int")
        if not self.is_an_int(second):
            raise ValueError("Error: Second parameter for range parameter isn't an int")
        return True

    def are_ranges_ints(self, strg, search=re.compile(r'[^a-z0-9,]').search):
        return not bool(search(strg))

    def is_an_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def compare_with_rules(self, rules, keywords):
        """
        This function will test `keyword` against every entry of the list `rules`.

        :param rules: Rules list containing all authorized rules
        :param keywords: The keywords to test
        :return: If `keywords` isn't found, `False` is returned. `True` otherwise
        """
        for i, s in enumerate(keywords):
            if s not in rules:
                return False
        return True
