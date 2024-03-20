import pytest
import pdb
from unittest.mock import patch
from io import StringIO

from exercs.assessment2_v2 import signup as t1
from exercs.assessment2 import signup as t2

@pytest.mark.parametrize("input_values, expected_output", [
    (["John Doe", "0123456789", "31/12/2000", "Password@123", "Password@123"], "Signup process completed successfully."),
    (["John Doe", "123456789", "31/12/2000", "Password@123", "Password@123"], "Invalid mobile number. Please start again."),
    (["John Doe", "0123456789", "31-12-2000", "Password@123", "Password@123"], "Invalid date of birth format. Please start again."),
    (["John Doe", "0123456789", "31/12/2000", "Password123", "Password123"], "Invalid password format. Please start again."),
    (["John Doe", "0123456789", "31/12/2000", "Password@123", "Password@321"], "Passwords do not match. Please start again."),
    (["John Doe", "0123456789", "31/12/2000", "0pass@123", "0pass@123"], "Invalid password format. Please start again.")
])
def test_t1(input_values, expected_output):
    with patch('builtins.input', side_effect=input_values):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            t1()
            assert mock_stdout.getvalue().strip() == expected_output

@pytest.mark.parametrize("input_values, expected_output", [
    (["John Doe", "0123456789", "31/12/2000", "Password@123", "Password@123"], "Signup process completed successfully."),
    (["John Doe", "123456789", "31/12/2000", "Password@123", "Password@123"], "Invalid mobile number. Please start again."),
    (["John Doe", "0123456789", "31-12-2000", "Password@123", "Password@123"], "Invalid date of birth format. Please start again."),
    (["John Doe", "0123456789", "31/12/2000", "Password123", "Password123"], "Invalid password format. Please start again."),
    (["John Doe", "0123456789", "31/12/2000", "Password@123", "Password@321"], "Passwords do not match. Please start again."),
    (["John Doe", "0123456789", "31/12/2000", "0pass@123", "0pass@123"], "Invalid password format. Please start again.")
])
def test_t2(input_values, expected_output):
    with patch('builtins.input', side_effect=input_values):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            t2()
            assert mock_stdout.getvalue().strip() == expected_output

if __name__ == "__main__":
    pytest.main()
