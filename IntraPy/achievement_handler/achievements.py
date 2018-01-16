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
    def __init__(self):
        self.rules = ['id', 'name', 'internal_name', 'kind', 'tier',
                      'description', 'pedago', 'visible', 'nbr_of_success',
                      'parent_id', 'image', 'created_at', 'updated_at', 'slug',
                      'position', 'reward', 'title_id']
        super().__init__()

    def get_achievements(self, **options):
        args = Args()
        options["rules"] = self.rules
        if args.hydrate_values(options) is False:
            raise ValueError("Options couldn't be extracted")
        achievements = self.api_get("/v2/achievements", args, "GET")
        if options.get("pretty", False):
            return json.dumps(achievements, indent=4, sort_keys=True)
        return achievements

    """
    @todo Add 'pretty' option
    @body The pretty option isn't possible in get_achievements_by_id and should be
    """

    def get_achievements_by_id(self, achievement_id: int):
        response = self.api_get_single("/v2/achievements/" + str(achievement_id), "GET")
        ret = json.loads(response.content)
        return ret

    def get_achievements_cursus(self, cursus_id, **options):
        args = Args()
        options["rules"] = self.rules
        if args.hydrate_values(options) is False:
            raise ValueError("Options couldn't be extracted")
        achievements = self.api_get("/v2/cursus/" + str(cursus_id) + "/achievements", args, "GET")
        if options.get("pretty", False):
            return json.dumps(achievements, indent=4, sort_keys=True)
        return achievements

    def get_achievements_campus(self, campus_id, **options):
        args = Args()
        options["rules"] = self.rules
        if args.hydrate_values(options) is False:
            raise ValueError("Options couldn't be extracted")
        achievements = self.api_get("/v2/campus/" + str(campus_id) + "/achievements", args, "GET")
        if options.get("pretty", False):
            return json.dumps(achievements, indent=4, sort_keys=True)
        return achievements
