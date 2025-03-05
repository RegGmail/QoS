# Python Beast Series
# Mastering Mocking in Python
# Testes mais complexos, envolvendo comportamento de conexao remota

import requests
from Network_timeout import fetch_data
from unittest.mock import patch

def test_fetch_data_timeout():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.Timeout

        result = fetch_data ("http://api/example.com")
        print (result)

    assert result == {"error": "---> Request timed out"}
