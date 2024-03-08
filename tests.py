import pytest
from unittest.mock import patch
from io import StringIO

from exercs.assessment1 import (validateCredentials,
                                calculateIncome,
                                calculateTemperature,
                                calculateCharges,
                                calculateDelivery,
                                calculateChange,
                                calculateAverageSale,
                                calculateCapacity,
                                calculateAge)

def test_validateCredentials(monkeypatch, capsys):
    # Test valid credentials
    valid_test_cases = [
        ("1234567890", "P@s$word$1"),  # Valid mobile number and password
        ("9876543210", "Abc@123$4")     # Another valid mobile number and password
    ]

    for mobile_number, password in valid_test_cases:
        # Mock inputs for mobile number and password
        inputs = [mobile_number, password]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        validateCredentials()
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
        validateCredentials()
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
        validateCredentials()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Invalid credentials"

    # Test invalid special character
    inputs=["1234567890","Password1"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))  # Missing special character
    validateCredentials()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Invalid credentials"

    # Test invalid digit at the end
    inputs=["1234567890","Abc@defg"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0)) # Missing digit at the end
    validateCredentials()
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


@pytest.mark.parametrize("user_input, expected_output", [
    (("P001", 200, 10, 160, 4, 100), "Change to be returned to the customer (In Dollars) against Invoice number P001 is: 53.50"),
    (("P002", 150.25, 0, 150.25, 0, 0), "Change to be returned to the customer (In Dollars) against Invoice number P002 is: 0.00"),
    (("P003", 300, 50, 250, 5, 50), "Outstanding amount against Invoice number P003 and need to be paid by customer: 13.00"),
    (("P004", 75, 25, 50, 0, 25), "Outstanding amount against Invoice number P004 and need to be paid by customer: 0.25"),
    (("P005", 100, 0, 100, 0, 0), "Change to be returned to the customer (In Dollars) against Invoice number P005 is: 0.00"),
])
def test_calculateChange(user_input, expected_output):

    with patch('builtins.input', side_effect=user_input):
        with patch('builtins.print') as mocked_print:
            calculateChange()
            mocked_print.assert_called_with(expected_output)

@pytest.mark.parametrize("current_sales, current_visitors, last_sales, last_visitors, expected_output", [
    ([100, 200, 300], [50, 100, 150], [90, 180, 270], [45, 90, 135], "The average per person sale for the current weekend is the same as the last weekend."),
    ([100, 200, 300], [50, 100, 150], [110, 220, 330], [55, 110, 165], "The average per person sale for the current weekend is the same as the last weekend."),
    ([100, 200, 300], [50, 100, 150], [100, 200, 300], [50, 100, 150], "The average per person sale for the current weekend is the same as the last weekend."),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], "The average per person sale for the current weekend is the same as the last weekend."),
    ([10, 20, 30], [5, 10, 15], [10, 20, 30], [5, 10, 15], "The average per person sale for the current weekend is the same as the last weekend."),
    ([10, 20, 30], [5, 10, 15], [20, 40, 60], [10, 20, 30], "The average per person sale for the current weekend is the same as the last weekend."),
    ([10, 20, 30], [5, 10, 15], [6, 12, 18], [3, 6, 9], "The average per person sale for the current weekend is the same as the last weekend."),
    ([10, 20, 30], [5, 10, 15], [8, 16, 24], [4, 8, 12], "The average per person sale for the current weekend is the same as the last weekend.")
])
def test_calculateAverageSale(current_sales, current_visitors, last_sales, last_visitors, expected_output):
    with patch('builtins.input', side_effect=current_sales + current_visitors + last_sales + last_visitors):
        with patch('builtins.print') as mocked_print:
            calculateAverageSale()
            mocked_print.assert_called_with(expected_output)


@pytest.mark.parametrize("width, length, expected_output", [
    (200, 300, "The restaurant can accommodate 4 person(s).\n"),
    (400, 500, "The restaurant can accommodate 15 person(s).\n"),
    (1000, 1000, "A maximum of 70 persons are allowed.\nThe restaurant can accommodate 70 person(s).\n"),
])
def test_calculateCapacity(width, length, expected_output):
    input_values = f"{width}\n{length}\n"

    with patch("builtins.input", side_effect=input_values.split("\n")), patch("sys.stdout", new_callable=StringIO) as output:
        calculateCapacity()
        assert output.getvalue() == expected_output



@pytest.mark.parametrize("customer_name, customer_birth, customer_city, customer_mobile, customer_email, expected_output", [
    ("John Doe", "1990", "New York", "123456789", "john.doe@example.com",
     "\nGreetings, John Doe!\nHere are your details:\n Year of Birth: 1990\n City: New York\n Email: john.doe@example.com\n Mobile: 123456789\n"),
    ("Alice Smith", "2000", "Los Angeles", "987654321", "alice.smith@example.com",
     "\nGreetings, Alice Smith!\nHere are your details:\n Year of Birth: 2000\n City: Los Angeles\n Email: alice.smith@example.com\n Mobile: 987654321\n"),
])
def test_calculateAge(customer_name, customer_birth, customer_city, customer_mobile, customer_email, expected_output, monkeypatch, capsys):
    inputs = [customer_name, customer_birth, customer_city, customer_mobile, customer_email]
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: inputs.pop(0))
        calculateAge()
        captured = capsys.readouterr()
        assert captured.out == expected_output
