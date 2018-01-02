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
    """
    options = {}

    def __init__(self):
        # TODO: Add test here to test if options != NULL etc
        self.page_number = None
        self.page_size = None
        self.sort = None
        self.filter = None
        self.range = None
        self.page_index = None
        self.all_pages = None

    def hydrate_values(self, options):
        self.all_pages = options.get("all_pages", False)
        if self.all_pages is True:
            self.page_index = 1
        else :
            self.page_index = options.get("page_number", 1)
        self.page_number = options.get("page_number", 1)# TODO GESTION ERREUR STR -> INT (page_number="LOL")
        self.page_size = options.get("page_size", 30) if \
            options.get("page_size", 30) <= 100 else 100
        if self.check_keywords(options) is False:
            return False
        else:
            self.sort = options.get("sort", False)
            self.filter = options.get("filter", False)  # TODO check if works
        self.check_keywords(options)

    def check_keywords(self,options):
        if "rules" not in options: # S'il n'y a pas de regle, l'api de 42 les ignorera =D
            return True
        if self.sanitize_keyword_string(options.get("sort", "id"),
                                        options["rules"]) is False:
            print("ERROR : Wrong parameters for 'sort' option") # TODO: Error message with wrong parameter
            return False
        #if self.sanitize_keyword_brackets(options.get("filter", "id"),
        #                                options["rules"]) is False:
        #    print("ERROR : Wrong parameters for 'filter' option")
        #    return False
        return True

    def sanitize_keyword_string(self, string, rules):
        keyword = string.split(',') # cree une liste de chaque mot
        for i, s in enumerate(keyword):
            keyword[i] = re.sub(r'-', '', s) #enleve les '-' avant la comparaison
        return self.compare_with_rules(rules, keyword)

    def sanitize_keyword_brackets(self, string, rules):
        keyword = re.search('[.*]', string)
        return self.compare_with_rules(rules, keyword)

    def compare_with_rules(self, rules, keyword):
        for i, s in enumerate(keyword):
            if s not in rules: #verifie que le mot soit dans les regles envoye par la classe initiale
                return False
        return True
