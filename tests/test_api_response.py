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

# nosetests --verbosity=2
# https://realpython.com/blog/python/testing-third-party-apis-with-mocks/

from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none
from IntraPy.services import get_accreditation_service


@patch('IntraPy.IntraPy.requests.request')
def test_request_response(mock_get):
    mock_get.return_value.ok = True
    response = get_accreditation_service()
    assert_is_not_none(response)
