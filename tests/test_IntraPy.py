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
from nose.tools import assert_is_not_none, assert_equal
from unittest.mock import Mock, patch
from IntraPy.IntraPy import IntraPy
import json


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
    mock_get.return_value.ok = False
    api = IntraPy()
    response = api.api_get_single("/v2/thisdoesntexist")
    assert_is_not_none(response)

"""
def test_get_uid_from_token():
    # We are patching the specified function
    mock_get_patcher = patch('IntraPy.IntraPy.requests.request')
    # What we want the json to be
    info = [{
        "resource_owner_id": "Null",
        "scopes":["public"],
        "expires_in_seconds": 0000,
        "application":
            {
                "uid":"8ngp6jutwr7ge667eqsnqqacppk7wkv2v6hk7rdtvbtzfu82krdeakg3x4rvcra3"
            },
        "created_at": 0000000
    }]
    # Call an instance of the desired class before the mock (Necessary here)
    api = IntraPy()
    # Start patching 'requests.request'.
    mock_get = mock_get_patcher.start()

    # Configure the mock to return a response with status code 200 and the info
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.content = json.dumps(info)

    # Call the service, which will send a request to the server.
    response = api.get_uid_from_token()

    # Stop patching 'requests'.
    mock_get_patcher.stop()

    # Assert that the request-response cycle completed successfully.
    assert_equal(response.status_code, 200)
    assert_equal(response.json(), info)
"""