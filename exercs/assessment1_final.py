#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:34:00 2024

@author: Gustavo Moraes Souza
"""

"""
1. Customers details: You are requested to enable the customer to insert their details to create a
new account. Each customer will be asked to insert the following:
a) the customer’s name,
b) mobile number,
c) year of birth,
d) current city
e) email address to register for promotions.
The application must calculate the customer's age (assume the current year is always 2023) and
confirm to the customer with a greeting message by displaying all the details if the customer is more
than 21 years of age.
"""

# # Data inputs
# customer_name = input("Please, enter customer name: ")
# customer_birth = int(input("Year of birth: "))
# customer_city = input("Current city: ")
# customer_mobile = input("Mobile number: ")
# customer_email = input("Email: ")

# current_year = 2023

# if current_year - customer_birth >= 21:
#     print("\nGreetings,", customer_name, "!\nHere are your details:\n Year of Birth: ", customer_birth, "\n City: ", customer_city,"\n Email: ", customer_email ,"\n Mobile: ", customer_mobile,"")


"""
2. Restaurant Capacity: Write a program to advise the restaurant manager on how many customers
the restaurant can accommodate based on the restaurant dimensions. Your program will ask the
manager to insert the width and length of the restaurant in centimetres. Assuming that a person
occupies 1.3 square meters of space. The program should output the number of people that can be
accommodated in the restaurant (The output should be an integer).
Note: if the calculated number of people that the restaurant can accommodate is more than 70, the
program must print the message that A Maximum of 70 persons are allowed.
 
"""
# # Constants
# PERSON_SPACE = 1.3  # Square meters per person
# MAX_PERSONS = 70  # Maximum number of persons allowed

# # Input dimensions from the manager
# width = float(input("Enter the width of the restaurant in centimeters: "))
# length = float(input("Enter the length of the restaurant in centimeters: "))

# # Calculate area in square meters
# area = (width / 100) * (length / 100)

# # Calculate number of persons
# num_persons = int(area / PERSON_SPACE)

# # Check if number of persons exceeds the maximum limit
# if num_persons > MAX_PERSONS:
#     num_persons = MAX_PERSONS
#     print("A maximum of 70 persons are allowed.")

# # Output the result
# print("The restaurant can accommodate ", num_persons ," person(s).")

"""
3. At the end of each week the manager would like to assess the average per person sale and
compare it to the previous weekend. Write a program to ask the manager for the following input:

I. Current weekend’s day wise sale and number of persons visited.
II. Last weekend’s day wise sale and number of persons visited.

Calculation:
Note:
1- Current Weekend’s per person average sale = Total sale for Current weekend / Total number of persons visited in the Current Weekend
2- Last Weekend’s per person average sale = Total sale for Last weekend / Total number of persons visited in the Last Weekend

You must use a list.
The weekend includes Friday, Saturday, and Sunday.
"""

# # Function to calculate average per person sale

# current_weekend_sales = []
# current_weekend_visitors = []
# last_weekend_sales = []
# last_weekend_visitors = []

# # Input current weekend's sales and visitors
# print("Enter the sales and visitors for the current weekend:")

# current_sales_friday = float(input("Enter sales for Friday: "))
# current_sales_saturday = float(input("Enter sales for Saturday: "))
# current_sales_sunday = float(input("Enter sales for Sunday: "))

# current_weekend_sales.append(current_sales_friday)
# current_weekend_sales.append(current_sales_saturday)
# current_weekend_sales.append(current_sales_sunday)

# current_visitors_friday = int(input("Enter number of visitors for Friday: "))
# current_visitors_saturday = int(input("Enter number of visitors for Saturday: "))
# current_visitors_sunday = int(input("Enter number of visitors for Sunday: "))

# current_weekend_visitors.append(current_visitors_friday)
# current_weekend_visitors.append(current_visitors_saturday)
# current_weekend_visitors.append(current_visitors_sunday)

# # Input last weekend's sales and visitors
# print("\nEnter the sales and visitors for the last weekend:")

# last_sales_friday = float(input("Enter sales for Friday: "))
# last_sales_saturday = float(input("Enter sales for Saturday: "))
# last_sales_sunday = float(input("Enter sales for Sunday: "))

# last_weekend_sales.append(last_sales_friday)
# last_weekend_sales.append(last_sales_saturday)
# last_weekend_sales.append(last_sales_sunday)

# last_visitors_friday = int(input("Enter number of visitors for Friday: "))
# last_visitors_saturday = int(input("Enter number of visitors for Saturday: "))
# last_visitors_sunday = int(input("Enter number of visitors for Sunday: "))

# last_weekend_visitors.append(last_visitors_friday)
# last_weekend_visitors.append(last_visitors_saturday)
# last_weekend_visitors.append(last_visitors_sunday)

# # Calculate total sales and visitors for both weekends
# total_current_sales = current_weekend_sales[0] + current_weekend_sales[1] + current_weekend_sales[2]
# total_current_visitors = current_weekend_visitors[0] + current_weekend_visitors[1] + current_weekend_visitors[2]
# total_last_sales = last_weekend_sales[0] + last_weekend_sales[1] + last_weekend_sales[2]
# total_last_visitors = last_weekend_visitors[0] + last_weekend_visitors[1] + last_weekend_visitors[2] 

# average_current_sale = 0
# average_last_sale = 0

# # Calculate average per person sale for both weekends
# if total_current_visitors > 0: 
#     average_current_sale = total_current_sales / total_current_visitors

# if total_last_visitors > 0:
#     average_last_sale = total_last_sales / total_last_visitors

# # Output the results
# print("\nCurrent Weekend's Average Per Person Sale: " , average_current_sale, "\n")
# print("Last Weekend's Average Per Person Sale: " , average_last_sale, "\n")

# # Compare the results
# if average_current_sale > average_last_sale:
#     print("The average per person sale for the current weekend is higher than the last weekend.")
# elif average_current_sale < average_last_sale:
#     print("The average per person sale for the current weekend is lower than the last weekend.")
# else:
#     print("The average per person sale for the current weekend is the same as the last weekend.")

"""
4. Create a program to calculate and print the amount of change to be returned to the customer,
after paying the bill, based on the manager's inputs in the system.
 
Sample Input:
Invoice Number:  P001
Total Invoice amount (In Dollars): 200
Amount of Tip (In Cents): 10
Total Payment received by Card: 160
Service Charge on Payment made by Card: 4%
Total Payment received in Cash (In Dollars): 100

Output:
Change to be returned to the customer (In Dollars)
against Invoice number P001 is: 53.50

Note: If the return to customer amount is negative, then it must print “Outstanding amount against
Invoice number P001 and need to be paid by customer:”, and the amount need to be paid.
"""

# # Input invoice details
# invoice_number = input("Invoice Number: ")
# total_invoice_amount = float(input("Total Invoice amount (In Dollars): "))
# tip_amount_cents = int(input("Amount of Tip (In Cents): "))
# total_payment_card = float(input("Total Payment received by Card: "))
# service_charge = float(input("Service Charge on Payment made by Card (%): "))
# total_payment_cash = float(input("Total Payment received in Cash (In Dollars): "))

# # Convert to cents
# total_payment_card_cents = total_payment_card * 100
# total_payment_cash_cents = total_payment_cash * 100

# # Calculate service charge amount
# service_charge_amount_cents = (service_charge / 100) * total_payment_card_cents

# # Calculate total amount paid by card including service charge
# total_amount_paid_by_card_cents = total_payment_card_cents - service_charge_amount_cents

# total_amount_paid_by_cash_cents = total_payment_cash_cents - tip_amount_cents

# # Calculate total amount paid in cents
# total_payment_received_cents = total_amount_paid_by_card_cents + total_amount_paid_by_cash_cents

# # Calculate total invoice amount in cents
# total_invoice_amount_cents = total_invoice_amount * 100

# # Calculate total change to be returned
# change_to_return_cents = total_payment_received_cents - total_invoice_amount_cents

# # Convert change to be returned to dollars
# change_to_return_dollars = change_to_return_cents / 100

# # Output the result
# if change_to_return_dollars >= 0:
#     print("Change to be returned to the customer (In Dollars) against Invoice number ", invoice_number," is: ", change_to_return_dollars)
# else:
#     outstanding_amount = -change_to_return_dollars
#     print("Outstanding amount against Invoice number ", invoice_number," and need to be paid by customer: ", outstanding_amount)


"""
5. Write the program to provide the user with an amount he/she needs to pay including the delivery
and packaging charges. The program should ask the user for the following input:

a) His full address
b) The amount of order placed
c) The distance in KM between the address provided and the restaurant

The total charges must be calculated based on the bellow rates:
Packaging Charges for:
• Order Amount more than 20 AUD to 35 AUD : 10%
• Order Amount more than 35 AUD to 50 AUD : 8%
• Order Amount more than 50 AUD : 6%

Delivery Charges for:
i. More than 0 to 4 Kilometres : $3
ii. More than 4 to 8 Kilometres : $6
iii. More than 8 to 12 Kilometres : $10
iv. More than 12 Kilometres : No Delivery can be done

Based on the input entered by the user the program must calculate and displays the all the details
effectively.
"""

# Input user details
full_address = input("Enter your full address: ")
order_amount = float(input("Enter the amount of the order placed (in AUD): "))
distance_km = float(input("Enter the distance in kilometers: "))

delivery_charges = None

# Calculate packaging charges
if 20 < order_amount <= 35:
    packaging_charge_percentage = 0.10
elif 35 < order_amount <= 50:
    packaging_charge_percentage = 0.08
elif order_amount > 50:
    packaging_charge_percentage = 0.06
else:
    packaging_charge_percentage = 0

packaging_charges = order_amount * packaging_charge_percentage

# Calculate delivery charges
if 0 < distance_km <= 4:
    delivery_charges = 3
elif 4 < distance_km <= 8:
    delivery_charges = 6
elif 8 < distance_km <= 12:
    delivery_charges = 10
else:
    delivery_charges = None

# Calculate total amount to be paid
if delivery_charges is not None:
    total_amount = order_amount + packaging_charges + delivery_charges
    print("\nDelivery Details:"
    "\nDelivery to: {}"
    "\nDistance: {} km"
    "\nDelivery charges: ${}"
    "\nOrder Details:"
    "\nOrder amount: ${}"
    "\nPackaging charges: ${}"
    "\nTotal amount to be paid (including delivery and packaging charges): ${}".format(full_address,
                                                                                        distance_km,
                                                                                        delivery_charges,
                                                                                        order_amount,
                                                                                        packaging_charges,
                                                                                        total_amount))
else:
    print("No delivery can be done for a distance greater than 12 kilometers.")


# """
# 6. Write a program to calculate the total charges of a placed order at the restaurant. Additional
# charges apply based on the order type selected from the options of:
# 1- dine in: Additional service charges of 8% apply
# 2- pick up: no additional charges
# 3- delivery: additional delivery charges of 10% apply

# The program should ask the user to insert the order base cost in AUD and the order type (1 or 2 or 3), and then the program should output the total amount to be paid.
# """

# # Input order details
# order_base_cost = float(input("Enter the order base cost (in AUD): "))
# order_type = int(input("Enter the order type (1 for dine in, 2 for pick up, 3 for delivery): "))
# additional_charges_percentage = 0

# # Calculate additional charges based on order type
# if order_type == 1:  # dine in
#     additional_charges_percentage = 0.08

#     # Calculate total charges
#     total_charges = order_base_cost + order_base_cost * additional_charges_percentage
#     # Output the result
#     print(f"Total charges for the order: ${total_charges:.2f}")

# elif order_type == 2:  # pick up
#     additional_charges_percentage = 0

#     # Calculate total charges
#     total_charges = order_base_cost + order_base_cost * additional_charges_percentage
#     # Output the result
#     print(f"Total charges for the order: ${total_charges:.2f}")

# elif order_type == 3:  # delivery
#     additional_charges_percentage = 0.10

#     # Calculate total charges
#     total_charges = order_base_cost + order_base_cost * additional_charges_percentage
#     # Output the result
#     print(f"Total charges for the order: ${total_charges:.2f}")

# else:
#     print("Invalid order type!")
    
# """
# 7. Write a temperature conversion program. The program should offer two forms of conversions:
# 1- from Centigrade to Fahrenheit
# 2-From Fahrenheit to Centigrade
# The program should ask the user to insert the temperature value and then conversion option (1 or 2).
# ••• The program should output the converted temperature.
# Your program should print a warning message for invalid values of temperature.
# Any Other option selected: Invalid Entry.
# """

# # Input temperature and conversion type
# temperature = float(input("Enter the temperature value: "))
# conversion_type = int(input("Enter the conversion type (1 for Centigrade to Fahrenheit, 2 for Fahrenheit to Centigrade): "))

# # Perform the conversion based on the conversion type
# if conversion_type == 1:
#     converted_temperature = (temperature * 9/5) + 32
#     print(f"{temperature} Celsius is equal to {converted_temperature:.2f} Fahrenheit.")
# elif conversion_type == 2:
#     converted_temperature = (temperature - 32) * 5/9
#     print(f"{temperature} Fahrenheit is equal to {converted_temperature:.2f} Celsius.")
# else:
#     print("Invalid Entry!")

# """
# 8. Write a program to help the manager calculating the net monthly income of the employee after
# the tax is deducted. Assume a fixed income tax of 18 %. The program should ask the manager to
# insert the following input:
# a) the position of the employee (chef, waiter, delivery or cleaner).
# b) the number of monthly hours the employee worked.
# If hours are entered in decimal format, the calculations will be executed by rounding the hours to the nearest positive value.
# The pay rate is calculated as follows:
# • Chef $30 Per hour,
# • Waiter $28 Per hour,
# • Delivery $25 Per hour,
# • Cleaner $ 24 Per hour
# Note: you should ensure a correct output regardless of the input case (upper case, lower case and more).
# """

# # Pay rates per hour for each position
# pay_rates = {
#     "chef": 30,
#     "waiter": 28,
#     "delivery": 25,
#     "cleaner": 24
# }

# # Input employee details
# position = input("Enter the position of the employee (chef, waiter, delivery, or cleaner): ").lower()
# monthly_hours_worked = float(input("Enter the number of monthly hours the employee worked: "))

# # Round the hours to the nearest positive value
# rounded_hours_worked = monthly_hours_worked

# # Calculate the gross monthly income
# hourly_rate = pay_rates.get(position, 0)
# gross_income = hourly_rate * rounded_hours_worked

# # Calculate the income tax
# income_tax_percentage = 0.18
# income_tax = gross_income * income_tax_percentage

# # Calculate the net monthly income
# net_income = gross_income - income_tax

# # Output the result
# print(f"Position: {position.capitalize()}")
# print(f"Monthly Hours Worked: {rounded_hours_worked}")
# print(f"Gross Monthly Income: ${gross_income:.2f}")
# print(f"Income Tax (18%): ${income_tax:.2f}")
# print(f"Net Monthly Income: ${net_income:.2f}")

# finalList = [position.capitalize(),rounded_hours_worked,gross_income,income_tax,net_income]
# print(finalList)

# """
# 9. Create a program that ask the user to enter user credential signing up a new account. The
# program should ask the user to insert the following:
# 1. mobile number
# 2. password

# The program should print the output “Valid credentials” if:
# 1. the mobile number is having exactly 10 digits.
# 2. the password has a minimum of 7 characters and maximum 11 characters.
# 3. The password must contain at least one special character, either @ or $
# 4. The password must end with a digit
# Note: The program should print “invalid credentials” otherwise.
# """

# # Input user credentials
# mobile_number = input("Enter your mobile number: ")
# password = input("Enter your password: ")
# digits = (1,2,3,4,5,6,7,8,9,0)

# # Check mobile number
# if len(mobile_number) != 10:
#     print("Invalid credentials")
# else:
#     # Check password length
#     if len(password) < 7 or len(password) > 11:
#         print("Invalid credentials")
#     else:
#         if not password[-1] in digits:
#             print("Invalid credentials")
#         else:
#             # Check for at least one special character and ending with a digit
#             special_chars = ('@','$')
#             if not special_chars[0] in password and not special_chars[1] in password:
#                 print("Invalid credentials")
#             else:
#                 print("Valid credentials")
