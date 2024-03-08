#!/usr/bin/python3
def calculateChange():
    # Input invoice details
    invoice_number = input("Invoice Number: ")
    total_invoice_amount = float(input("Total Invoice amount (In Dollars): "))
    tip_amount_cents = int(input("Amount of Tip (In Cents): "))
    total_payment_card = float(input("Total Payment received by Card: "))
    service_charge = float(input("Service Charge on Payment made by Card (%): "))
    total_payment_cash = float(input("Total Payment received in Cash (In Dollars): "))

    # Convert to cents
    total_payment_card_cents = total_payment_card * 100
    total_payment_cash_cents = total_payment_cash * 100

    # Calculate service charge amount
    service_charge_amount_cents = (service_charge / 100) * total_payment_card_cents

    # Calculate total amount paid by card including service charge
    total_amount_paid_by_card_cents = total_payment_card_cents - service_charge_amount_cents

    total_amount_paid_by_cash_cents = total_payment_cash_cents - tip_amount_cents

    # Calculate total amount paid in cents
    total_payment_received_cents = total_amount_paid_by_card_cents + total_amount_paid_by_cash_cents
    
    # Calculate total invoice amount in cents
    total_invoice_amount_cents = total_invoice_amount * 100

    # Calculate total change to be returned
    change_to_return_cents = total_payment_received_cents - total_invoice_amount_cents
    
    # Convert change to be returned to dollars
    change_to_return_dollars = change_to_return_cents / 100
    
    # Output the result
    if change_to_return_dollars >= 0:
        print(f"Change to be returned to the customer (In Dollars) against Invoice number {invoice_number} is: {change_to_return_dollars:.2f}")
    else:
        outstanding_amount = -change_to_return_dollars
        print(f"Outstanding amount against Invoice number {invoice_number} and need to be paid by customer: {outstanding_amount:.2f}")

# Test the function
calculateChange()
