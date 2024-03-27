import pytest
from unittest.mock import patch
from io import StringIO

from exercs.assessment2_v4 import signup 
from exercs.assessment2_v4 import login 

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




# def test_reset_password_successful_login(users):
#     users.append({'full_name': 'John Doe', 'contact_number': '0123456789', 'dob': '31/12/2000', 'password': 'Password@123'})
#     input_values = ["0123456789", "Password@123", "1", "Password@123", "Password@456", "2"]
#     expected_output = [
#         "You have successfully signed in.\nWelcome John Doe",
#         "Please enter:\n1 for resetting the password.\n2 for sign out.",
#         "Please enter your old password: ",
#         "Please enter your new password: ",
#         "Your password has been reset successfully.",
#         "Please enter:\n1 for resetting the password.\n2 for sign out."
#     ]
#     with patch('builtins.input', side_effect=input_values):
#         with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#             login(users)
#             output = mock_stdout.getvalue().strip().split('\n')
#             assert output[:len(expected_output)] == expected_output

# def test_reset_password_unsuccessful_login_attempts(users):
#     users.append({'full_name': 'John Doe', 'contact_number': '0123456789', 'dob': '31/12/2000', 'password': 'Password@123'})
#     input_values = ["0123456789", "WrongPassword", "0123456789", "WrongPassword", "0123456789", "WrongPassword", "0123456789", "31/12/2000", "Password@123", "Password@123", "Password@456", "2"]
#     expected_output = [
#         "Incorrect contact number or password. Please try again.",
#         "Incorrect contact number or password. Please try again.",
#         "Incorrect contact number or password. Please try again.",
#         "You have used the maximum attempts of login.\nPlease reset the password by entering the below details:\nPlease enter your Username (Mobile Number) to confirm: ",
#         "Please enter you Date of Birth in DD/MM/YYYY format, to confirm: ",
#         "Please enter your new password: ",
#         "Your password has been reset successfully.",
#         "Please enter:\n1 for resetting the password.\n2 for sign out."
#     ]
#     with patch('builtins.input', side_effect=input_values):
#         with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#             login(users)
#             output = mock_stdout.getvalue().strip().split('\n')
#             assert output[:len(expected_output)] == expected_output

def test_signup_successful(users):
    input_values = ["John Doe", "0123456789", "31/12/2000", "Password@123", "Password@123"]
    expected_output = "Signup process completed successfully."
    with patch('builtins.input', side_effect=input_values):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            assert signup(users) is True
            output = mock_stdout.getvalue().strip()
            assert output == expected_output

def test_signup_invalid_mobile_number(users):
    input_values = ["John Doe", "123456789", "31/12/2000", "Password@123", "Password@123"]
    expected_output = "Invalid mobile number. Please start again."
    with patch('builtins.input', side_effect=input_values):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            assert signup(users) is False
            output = mock_stdout.getvalue().strip()
            assert output == expected_output

def test_signup_invalid_password(users):
    input_values = ["John Doe", "0123456789", "31/12/2000", "pass123", "pass123"]
    expected_output = "Invalid password format. Please start again."
    with patch('builtins.input', side_effect=input_values):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            assert signup(users) is False
            output = mock_stdout.getvalue().strip()
            assert output == expected_output

def test_signup_passwords_not_matching(users):
    input_values = ["John Doe", "0123456789", "31/12/2000", "Password@123", "Password@456"]
    expected_output = "Passwords do not match. Please start again."
    with patch('builtins.input', side_effect=input_values):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            assert signup(users) is False
            output = mock_stdout.getvalue().strip()
            assert output == expected_output

def test_signup_invalid_dob(users):
    input_values = ["John Doe", "0123456789", "31-12-2000", "Password@123", "Password@123"]
    expected_output = "Invalid date of birth format. Please start again."
    with patch('builtins.input', side_effect=input_values):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            assert signup(users) is False
            output = mock_stdout.getvalue().strip()
            assert output == expected_output

def test_signup_age_below_21(users):
    input_values = ["John Doe", "0123456789", "31/12/2010", "Password@123", "Password@123"]
    expected_output = "You must be at least 21 years old to sign up. Please start again."
    with patch('builtins.input', side_effect=input_values):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            assert signup(users) is False
            output = mock_stdout.getvalue().strip()
            assert output == expected_output

if __name__ == "__main__":
    pytest.main()
