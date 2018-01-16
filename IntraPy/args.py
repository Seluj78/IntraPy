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

# @todo Add 'range' handling
# @body The `range` option isn't currently handled

    def __init__(self):
        self.page_number = None
        self.page_size = 30
        self.sort = None
        self.filter = None
        self.range = None
        self.from_page = None
        self.to_page = None
        self.pretty = False


# @todo Check if the option.get('filter') works correctly
# @body further test and error handling is needed on `self.filter = options.get("filter", False)`

    def hydrate_values(self, options):
        self.page_number = options.get("page_number", -1)
        if not isinstance(self.page_number, int):
            raise TypeError("page_number must be an int")
        if self.page_number > 0:  # ICI, page number a la priorite sur to and from pages
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
            self.filter = options.get("filter", False)
        self.check_keywords(options)

    def check_keywords(self, options):
        """
        This function will check if the keywords given to `filter` and `sort` are in the rules

        :param options: The options passed
        :return: Returns False is any keyword isn't in the authorized rules
        """
        # If there isn't any rules, the API will ignore them
        if "rules" not in options:
            return True
        if "sort" in options and self.sanitize_keyword_string(options.get("sort", "id"), options["rules"]) is False:
            raise ValueError("Wrong value for `sort` parameter.")
        if "filter" in options and self.sanitize_keyword_brackets(options.get("filter", "id"), options["rules"]) is False:
            raise ValueError("Wrong value for `filter` parameter.")
        return True

    def sanitize_keyword_string(self, string, rules):
        """
        This function will split the `sort` string `string` into keyword and compare
        each one to the given rules.

        :param string: The string to split into keywords
        :param rules: The rules authorized
        :return: Returns `False` if the sort options aren't in rules
        """

        # @todo Add multiple sorts
        # @body Multiple sort parameters isn't handled, eg. `sort="one"&sort="two"`

        if not isinstance(string, str):
            raise ValueError("sort must be a String")
        # Create a list (with separator `'`)containing each word
        keyword = string.split(',')
        # Remove `-` before comparison
        for i, s in enumerate(keyword):
            keyword[i] = re.sub(r'-', '', s)
        # Compare each Keyword with the rules
        return self.compare_with_rules(rules, keyword)

    def sanitize_keyword_brackets(self, string, rules):
        """
        This function will split the `filter` string `string` into keyword and compare
        each one to the given rules.

        :param string: The string to split into keywords
        :param rules: The rules authorized
        :return: Returns `False` if the filter options aren't in rules
        """
        # @todo Test the filter option
        # @body We haven't tested enough if the filter option works as intended

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
