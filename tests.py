import pytest
from exercs.assessment1 import (validate_credentials)

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