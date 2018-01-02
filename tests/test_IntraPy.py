from unittest import TestCase
from unittest.mock import Mock, patch
from nose.tools import assert_list_equal
from nose.tools import assert_is_none
from IntraPy.IntraPy import IntraPy


class TestIntraPy(TestCase):
    @patch('IntraPy.IntraPy.requests.request')
    def test_api_request_new_token(self, mock_get):
        fake_return = [{
            'access_token': 'df9580fc7b3c3501cb39646a89050c774ee3a43b3e55633345ef931ffecdf6e6',
            'token_type': 'bearer',
            'expires_in': 7200,
            'scope': 'public',
            'created_at': 1514886496
        }]
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = fake_return
        intra = IntraPy()
        response = intra.api_request_new_token()
        assert_list_equal(response, fake_return[0]['access_token'])

    @patch('IntraPy.IntraPy.requests.request')
    def test_api_request_new_token_fail(self, mock_get):
        mock_get.return_value.ok = False
        intra = IntraPy()
        response = intra.api_request_new_token()
        assert_is_none(response)
