# Python Beast Series
# Mastering Mocking in Python
# Testes mais complexos, envolvendo comportamento de conexao remota


import mock
from User_Authentication import User
from unittest.mock import patch

@mock.patch ('User_Authentication.login')

def test_user_authentication(mock_login):
    #mock_login = Mock()
    

    user = User()

    with patch ('User_Authentication.login', mock_login):

        mock_login.login.return_value = True
        response = mock_login.login("testuser", "password")
        print (response)

        assert user.login("testuser", "password") == True
    #mock_login.login.assert_called_once_with ("testuser", "password")

