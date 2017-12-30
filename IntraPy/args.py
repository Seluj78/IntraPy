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

from IntraPy import IntraPy
import re

class Args:
    """
        This will be the class for Args
    """
    options = {}

    def __init__(self):
       pass

    def hydrate_values(self,options):
        self.page_number = options.get("page_number", 1)
        self.page_size = options.get("page_size", 30) if options.get("page_size", 30) <= 100 else 100
        # TODO Renvoie une erreur
        if self.check_keywords(options) is False:
            return False
        else:
            self.sort = options.get("sort", "id")
        self.page_index = 1
        self.check_keywords(options)

    def check_keywords(self,options):
        if "rules" not in options: #S'il n'y a pas de regle, l'api de 42 les ignorera =D
            return True
        if self.sanitize_keyword_string(options.get("sort", "id"), options["rules"]) is False:
            print("ERROR : Wrong parameters for 'sort' option")
            return False
        return True

    def sanitize_keyword_string(self,str, rules):
        keyword = []
        keyword = str.split(',') #cree une liste de chaque mot
        for i, s in enumerate(keyword):
            keyword[i] = re.sub(r'-', '', s) #enleve les '-' avant la comparaison
        for i,s in enumerate(keyword):
            if s not in rules: #verifie que le mot soit dans les regles envoye par la classe initiale
                return False
        return True
