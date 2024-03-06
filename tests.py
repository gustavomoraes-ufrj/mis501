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
        "12345",    # Too short
        "1234567890a"  # Contains non-digit characters
    ]

    for mobile_number in invalid_mobile_numbers:
        monkeypatch.setattr('builtins.input', lambda _: mobile_number)
        monkeypatch.setattr('builtins.input', lambda _: "Password$1")
        validate_credentials()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Invalid credentials"

    # Test invalid password
    invalid_passwords = [
        "Pwd$1",            # Too short
        "Abcdefg$",         # Missing digit at the end
        "Abcdefghijkl$"     # Too long
    ]

    for password in invalid_passwords:
        monkeypatch.setattr('builtins.input', lambda _: "1234567890")
        monkeypatch.setattr('builtins.input', lambda _: password)
        validate_credentials()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Invalid credentials"

    # Test invalid special character
    monkeypatch.setattr('builtins.input', lambda _: "1234567890")
    monkeypatch.setattr('builtins.input', lambda _: "Password1")  # Missing special character
    validate_credentials()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Invalid credentials"

    # Test invalid digit at the end
    monkeypatch.setattr('builtins.input', lambda _: "1234567890")
    monkeypatch.setattr('builtins.input', lambda _: "Abc@defg")  # Missing digit at the end
    validate_credentials()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Invalid credentials"