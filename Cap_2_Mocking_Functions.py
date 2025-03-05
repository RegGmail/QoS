# Python Beast Series
# Mastering Mocking in Python

#
# Mocking functions and methods

from unittest.mock import patch

import Cap_2_User_Authentication

@patch ('Cap_2_User_Authentication.login')

def test_login (mock_login):
    mock_login.return_value = True

    result = Cap_2_User_Authentication.login("user", "password")

    assert result == True