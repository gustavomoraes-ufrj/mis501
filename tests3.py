import pytest
from unittest.mock import patch
from io import StringIO

from exercs.assessment2_v3 import signup 
from exercs.assessment2_v3 import login 

@pytest.fixture
def users():
    return []

@pytest.mark.parametrize("input_values, expected_output", [
    (["John Doe", "0123456789", "31/12/2000", "Password@123", "Password@123"], "Signup process completed successfully."),
    (["John Doe", "123456789", "31/12/2000", "Password@123", "Password@123"], "Invalid mobile number. Please start again."),
    (["John Doe", "0123456789", "31-12-2000", "Password@123", "Password@123"], "Invalid date of birth format. Please start again."),
    (["John Doe", "0123456789", "31/12/2000", "Password123", "Password123"], "Invalid password format. Please start again."),
    (["John Doe", "0123456789", "31/12/2000", "Password@123", "Password@321"], "Passwords do not match. Please start again."),
    (["John Doe", "0123456789", "31/12/2000", "0pass@123", "0pass@123"], "Invalid password format. Please start again.")
])

def test_signup(input_values, expected_output, users):
    with patch('builtins.input', side_effect=input_values):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            signup(users)
            assert mock_stdout.getvalue().strip() == expected_output

@pytest.mark.parametrize("input_values, expected_output, mock_users", [
    (["0123456789", "Password@123"], True, [{'full_name': 'John Doe', 'contact_number': '0123456789', 'dob': '31/12/2000', 'password': 'Password@123'}]),
    (["0123456789", "WrongPassword"], False, [{'full_name': 'John Doe', 'contact_number': '0123456789', 'dob': '31/12/2000', 'password': 'Password@123'}]),
    (["123456789", "Password@123"], False, [{'full_name': 'John Doe', 'contact_number': '0123456789', 'dob': '31/12/2000', 'password': 'Password@123'}]),
    (["0123456789", "Password@123"], False, []),
    (["0123456789", "Password@123"], False, [{'full_name': 'Jane Doe', 'contact_number': '9876543210', 'dob': '01/01/2000', 'password': 'Password@456'}]),
])
def test_login(input_values, expected_output, mock_users, users):
    users.extend(mock_users)
    with patch('builtins.input', side_effect=input_values):
        assert login(users) == expected_output

if __name__ == "__main__":
    pytest.main()
