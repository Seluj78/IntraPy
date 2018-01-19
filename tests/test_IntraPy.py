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
from nose.tools import assert_is_not_none
from unittest.mock import Mock, patch
from IntraPy.IntraPy import IntraPy


@patch('IntraPy.IntraPy.requests.request')
def test_api_with_good_url(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = True
    # Call the service, which will send a request to the server.
    api = IntraPy()
    response = api.api_get_single("/v2/achievements")
    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)


@patch('IntraPy.IntraPy.requests.request')
def test_api_with_bad_url(mock_get):
    # Configure the mock to return a response with an OK status code.
    mock_get.return_value.ok = False
    # Call the service, which will send a request to the server.
    api = IntraPy()
    response = api.api_get_single("/v2/thisdoesntexist")
    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)