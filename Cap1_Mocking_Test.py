# Python Beast Series
# Mastering Mocking in Python

from Cap1_MockBeast import get_user_data, process_user_data
from unittest.mock import patch


def test_process_user_data_1():

    mock_data = {'name':'John Doe', 'age':30}

    with patch('Cap1_MockBeast.get_user_data') as mock_get_user_data:
        mock_get_user_data.return_value = mock_data

        result = process_user_data(123)

        assert result == " ---> Usuario John Doe tem 30 anos de idade"

def test_process_user_data_2():

    mock_data = None


    with patch('Cap1_MockBeast.get_user_data') as mock_get_user_data:
        mock_get_user_data.return_value = mock_data

        result = process_user_data(456)

        assert result == " ***> Usuario nao encontrado"