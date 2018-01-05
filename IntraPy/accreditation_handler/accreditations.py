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


class Accreditations(IntraPy):
    def __init__(self):
        self.rules = []
        super().__init__()

    def get_accreditations(self, **options):
        args = Args()
        options["rules"] = self.rules
        if args.hydrate_values(options) is False:
            raise ValueError("Options couldn't be extracted")
        accreditations = self.api_get("/v2/accreditations", args, "GET")
        if options.get("pretty", False):
            return json.dumps(accreditations, indent=4, sort_keys=True)
        return accreditations

    def get_accreditations_by_id(self, accreditation_id: int):
        response = self.api_get_single("/v2/achievements/" + str(accreditation_id), "GET")
        accreditation = json.loads(response.content)
        return accreditation  # TODO: Pretty output possibility
