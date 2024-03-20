#!/usr/bin/python3

import pdb
from datetime import datetime
def debug(local, val):
    # Redirect the output to the file
    with open('debug.txt', 'a') as f:
        f.write(f"\n{local}: {val} \n")

# Function to validate mobile number
def validate_mobile_number(number):
    return number.isdigit() and len(number) == 10 and number.startswith('0')

# Function to validate password
def validate_password(password):
    if len(password) < 8:
        return False
    if not password[0].isalpha():
        return False
    if not password[-1].isdigit():
        return False
    special_chars = ('@', '&', '#')
    if not special_chars[0] in password and not special_chars[1] in password and not special_chars[2] in password:
        return False
    return True

# Function to validate date of birth
def validate_dob(dob):
    try:
        datetime.strptime(dob, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Function to calculate age based on date of birth
def calculate_age(dob):
    dob_year = int(dob.split('/')[2])
    current_year = datetime.now().year
    return current_year - dob_year

# Signup process
def signup():
    full_name = input("Enter your full name: ")
    contact_number = input("Enter your contact number: ")
    dob = input("Enter your date of birth (DD/MM/YYYY): ")
    password = input("Enter your password: ")
    password_confirmation = input("Confirm your password: ")

    pdb.set_trace()
    if not validate_mobile_number(contact_number):
        print("Invalid mobile number. Please start again.")
        return False

    if not validate_password(password):
        print("Invalid password format. Please start again.")
        return False

    if password != password_confirmation:
        print("Passwords do not match. Please start again.")
        return False

    if not validate_dob(dob):
        print("Invalid date of birth format. Please start again.")
        return False

    age = calculate_age(dob)
    if age < 21:
        print("You must be at least 21 years old to sign up. Please start again.")
        return False

    user_data = {
        'full_name': full_name,
        'contact_number': contact_number,
        'dob': dob,
        'password': password
    }

    # Save user_data in a data structure (e.g., list)
    print("Signup process completed successfully.")
    return True

def main():
  """ Main program  """ 
  while True:
      print("\nPlease enter:")
      print("1 for Sign up")
      print("2 for Sign in")
      print("3 for Quit application")

      choice = input("Your choice: ")

      if choice == '1':
          signup()
      elif choice == '2':
          # Implement sign in process
          pass
      elif choice == '3':
          print("Thank you for using the Application.")
          break
      else:
          print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()