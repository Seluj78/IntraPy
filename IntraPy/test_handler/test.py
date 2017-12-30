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
from IntraPy.utils import Utils


class Test(IntraPy, Args):

    def __init__(self):
        self.utils = Utils()
        self.rules = ['id', 'name', 'internal_name', 'kind', 'tier', 'description',
             'pedago', 'visible', 'nbr_of_success', 'parent_id', 'image', 'created_at',
             'updated_at', 'slug', 'position', 'reward', 'title_id']
        super().__init__()
        args = Args()

    def get_test(self, test_url: str, **options):
        str_url = "/v2/" + str(test_url)
        options["rules"] = self.rules
        args = Args()
        if args.hydrate_values(options) is False:
            return "ERROR : Options couldn't be extract"
        achievements = self.utils.get_all_pages(str_url, args)
        if options.get("pretty", False):
            return json.dumps(achievements, indent=4, sort_keys=True)
        return achievements
