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
    """
    This class handles all the accreditations that can be returned through
    the 42 API
    """
    def __init__(self):
        """
        Here, we simply initialize the parent class to have a simple access to
        other functions
        """
        self.rules = []
        super().__init__()

    def get_accreditations(self, **options):
        """
        This function will return all the accreditations, unless parameters
        specify otherwise like `page_number` or `from_page` and `to_page`999

        :param options: The kwargs options that can be passed paginate the accreditations
        :return: Returns a json list containing the requested accreditations
        """
        args = Args()
        options["rules"] = self.rules
        if args.hydrate_values(options) is False:
            raise ValueError("Options couldn't be extracted")
        accreditations = self.api_get("/v2/accreditations", args, "GET")
        if options.get("pretty", False):
            return json.dumps(accreditations, indent=4, sort_keys=True)
        return accreditations

    def get_accreditations_by_id(self, accreditation_id: int, pretty=False):
        """
        This function will return all the info sent by the API about
        the accreditation ID
        :param accreditation_id: The ID of the accreditation you want the ID from
        :param pretty: By default is set to False, this pretties up the output if printed

        :return: Returns a list in json form containing the requested accreditation
        """
        response = self.api_get_single("/v2/accreditations/" + str(accreditation_id), "GET")
        accreditation = json.loads(response.content)
        if pretty:
            return json.dumps(accreditation, indent=4, sort_keys=True)
        return accreditation
