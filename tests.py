import pytest
from unittest.mock import patch
from io import StringIO

from exercs.assessment1 import (validate_credentials,
                                calculateIncome,
                                calculateTemperature,
                                calculateCharges,
                                calculateDelivery)

def test_validate_credentials(monkeypatch, capsys):
    # Test valid credentials
    valid_test_cases = [
        ("1234567890", "Password$1"),  # Valid mobile number and password
        ("9876543210", "Abc@1234")     # Another valid mobile number and password
    ]

    for mobile_number, password in valid_test_cases:
        # Mock inputs for mobile number and password
        inputs = [mobile_number, password]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        validate_credentials()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Valid credentials"

    # Test invalid mobile number
    invalid_mobile_numbers = [
        ("12345","Password$1"),    # Too short
        ("1234567890a","Password$1")  # Contains non-digit characters
    ]

    for mobile_number, password in invalid_mobile_numbers:
        inputs=[mobile_number,password]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        validate_credentials()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Invalid credentials"

    # Test invalid password
    invalid_passwords = [
        ("1234567890","Pwd$1"),            # Too short
        ("1234567890","Abcdefg$"),         # Missing digit at the end
        ("1234567890","Abcdefghijkl$")     # Too long
    ]

    for mobile_number, password in invalid_passwords:
        inputs=[mobile_number,password]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        validate_credentials()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Invalid credentials"

    # Test invalid special character
    inputs=["1234567890","Password1"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))  # Missing special character
    validate_credentials()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Invalid credentials"

    # Test invalid digit at the end
    inputs=["1234567890","Abc@defg"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0)) # Missing digit at the end
    validate_credentials()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Invalid credentials"


@pytest.mark.parametrize("user_input, expected_output", [
    (("chef", 160), ["Chef", 160, 4800, 864, 3936]),
    (("waiter", 160), ["Waiter", 160, 4480, 806.4, 3673.6]),
    (("delivery", 160), ["Delivery", 160, 4000, 720, 3280]),
    (("cleaner", 160), ["Cleaner", 160, 3840, 691.1999999999999, 3148.8]),
    (("manager", 160), ["Manager", 160, 0, 0, 0])  # Manager position not in pay_rates
])
def test_calculateIncome(user_input, expected_output):
    with patch('builtins.input', side_effect=user_input):
        output = calculateIncome()
        assert output == expected_output


@pytest.mark.parametrize("user_input, expected_output", [
    ((25, 1), "25.0 Celsius is equal to 77.00 Fahrenheit."),
    ((77, 2), "77.0 Fahrenheit is equal to 25.00 Celsius."),
    ((100, 3), "Invalid Entry!")
])
def test_calculateTemperature(user_input, expected_output):
    with patch('builtins.input', side_effect=user_input):
        with patch('builtins.print') as mocked_print:
            calculateTemperature()
            mocked_print.assert_called_with(expected_output)



@pytest.mark.parametrize("user_input, expected_output", [
    ((30, 1), "Total charges for the order: $32.40"),
    ((25, 2), "Total charges for the order: $25.00"),
    ((50, 3), "Total charges for the order: $55.00"),
    ((40, 4), "Invalid order type!")
])
def test_calculateCharges(user_input, expected_output):
    with patch('builtins.input', side_effect=user_input):
        with patch('builtins.print') as mocked_print:
            calculateCharges()
            mocked_print.assert_called_with(expected_output)



@pytest.mark.parametrize("user_input, expected_output", [
    (("123 Main St", 30, 5), "\nDelivery Details:\nDelivery to: 123 Main St\nDistance: 5.0 km\nDelivery charges: $6\nOrder Details:\nOrder amount: $30.0\nPackaging charges: $3.0\nTotal amount to be paid (including delivery and packaging charges): $39.0"),
    (("456 Elm St", 45, 10), "\nDelivery Details:\nDelivery to: 456 Elm St\nDistance: 10.0 km\nDelivery charges: $10\nOrder Details:\nOrder amount: $45.0\nPackaging charges: $3.6\nTotal amount to be paid (including delivery and packaging charges): $58.6"),
    (("789 Oak St", 55, 15), "No delivery can be done for a distance greater than 12 kilometers.")
])
def test_calculateDelivery(user_input, expected_output):
    with patch('builtins.input', side_effect=user_input):
        with patch('builtins.print') as mocked_print:
            calculateDelivery()
            mocked_print.assert_called_with(expected_output)
