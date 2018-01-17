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
from IntraPy.args import Args


class Achievements(IntraPy):
    """
    This class handles all the achievements that can be retrieved through the
    42 API
    """
    def __init__(self):
        """
        Here, we initializes the parent class and creates a rule which contains
        all the sort/range/filter possibilities
        """
        self.rules = ['id', 'name', 'internal_name', 'kind', 'tier',
                      'description', 'pedago', 'visible', 'nbr_of_success',
                      'parent_id', 'image', 'created_at', 'updated_at', 'slug',
                      'position', 'reward', 'title_id']
        super().__init__()

    def get_achievements(self, **options):
        """
        This function will return all the achievements, unless parameters
        specify otherwise like `page_number` or `from_page` and `to_page`,
        or `sort` etc...

        :param options: The kwargs options that can be passed paginate/sort/filter/range the achievements
        :return: Returns a json list containing the requested achievements
        """
        args = Args()
        options["rules"] = self.rules
        if args.hydrate_values(options) is False:
            raise ValueError("Options couldn't be extracted")
        achievements = self.api_get("/v2/achievements", args, "GET")
        if options.get("pretty", False):
            return json.dumps(achievements, indent=4, sort_keys=True)
        return achievements

    def get_achievements_by_id(self, achievement_id: int, pretty=False):
        """
        This function will return all the info sent by the API about
        the achievements ID
        :param achievement_id: The ID of the achievements you want the ID from
        :param pretty: By default is set to False, this pretties up the output if printed

        :return: Returns a list in json form containing the requested achievement
        """
        response = self.api_get_single("/v2/achievements/" + str(achievement_id), "GET")
        achievement = json.loads(response.content)
        if pretty:
            return json.dumps(achievement, indent=4, sort_keys=True)
        return achievement

    def get_achievements_cursus(self, cursus_id, **options):
        """
        This function will return all the achievements from a given cursus,
        unless parameters specify otherwise like `page_number` or `from_page`
        and `to_page`, or `sort` etc...

        :param cursus_id: The cursus ID you want your achievements from
        :param options: The kwargs options that can be passed paginate/sort/filter/range the achievements
        :return: Returns a json list containing the requested achievements
        """
        args = Args()
        options["rules"] = self.rules
        if args.hydrate_values(options) is False:
            raise ValueError("Options couldn't be extracted")
        achievements = self.api_get("/v2/cursus/" + str(cursus_id) + "/achievements", args, "GET")
        if options.get("pretty", False):
            return json.dumps(achievements, indent=4, sort_keys=True)
        return achievements

    def get_achievements_campus(self, campus_id, **options):
        """
        This function will return all the achievements from a given campus,
        unless parameters specify otherwise like `page_number` or `from_page`
        and `to_page`, or `sort` etc...

        :param campus_id: The campus ID you want your achievements from
        :param options: The kwargs options that can be passed paginate/sort/filter/range the achievements
        :return: Returns a json list containing the requested achievements
        """
        args = Args()
        options["rules"] = self.rules
        if args.hydrate_values(options) is False:
            raise ValueError("Options couldn't be extracted")
        achievements = self.api_get("/v2/campus/" + str(campus_id) + "/achievements", args, "GET")
        if options.get("pretty", False):
            return json.dumps(achievements, indent=4, sort_keys=True)
        return achievements
