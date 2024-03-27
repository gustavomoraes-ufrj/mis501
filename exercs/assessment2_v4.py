#!/usr/bin/python3

import pdb
import os
import time
from datetime import datetime
def debug(local, val):
    # Redirect the output to the file
    with open('debug.txt', 'a') as f:
        f.write(f"\n{local}: {val} \n")

# Function to validate mobile number
def validate_mobile_number(number,users):
  if not number.isdigit():
    return False
  if not len(number) == 10:
    return False
  if not number.startswith('0'):
    return False
  
  for user in users:
    if user['contact_number'] == number:
      print("User already exists.")
      return False
  else:
    return True

# Function to validate password
def validate_password(password):
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
def signup(users):
  full_name = input("Enter your full name: ")
  contact_number = input("Enter your contact number: ")
  dob = input("Enter your date of birth (DD/MM/YYYY): ")
  password = input("Enter your password: ")
  password_confirmation = input("Confirm your password: ")

  if not validate_mobile_number(contact_number,users):
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

  users.append(user_data)
  print("Signup process completed successfully.")
  return True

# Login process
def login(users):
  contact_number = input("Enter your contact number: ")
  password = input("Enter your password: ")

  for user in users:
    if user['contact_number'] == contact_number:
      if user['password'] == password:
        print(f"You have successfully signed in.\nWelcome {user['full_name']}")
        while True:
          print("Please enter:")
          print("1 for resetting the password.")
          print("2 for sign out.")
          choice = input("Your choice: ")
          if choice == '1':
            if reset_password(user):
              print("Your password has been reset successfully.")
              return True
          elif choice == '2':
            print("You have signed out.")
            return True
          else:
            print("Invalid choice. Please try again.")
        # return True
      else:
        print("Incorrect password.")
        return False
  else:
    print("You have not signed up with this contact number. Please, signup first.")
    return False


# Reset password
def reset_password(user):
  old_password = input("Please enter your old password: ")
  if old_password == user['password']:
    new_password = input("Please enter your new password: ")
    if new_password != old_password:
      if validate_password(new_password):
        user['password'] = new_password
        return True
      else:
        print("Invalid new password.")
        return False
    else:
      print("You cannot use the password used earlier.")
      return False
  else:
    print("Incorrect old password.")
    return False

def main():
  """ Main program  """ 

  # Initialize users list
  users = []

  while True:
# Clear the screen based on the operating system
    os.system('clear')
    print("\nPlease enter:")
    print("Please Enter 1 for Sign up.")
    print("Please Enter 2 for Sign in.")
    print("Please Enter 3 for Quit.")

    choice = input("Your choice: ")

    if choice == '1':
      signup(users)
    elif choice == '2':
      login(users)
    elif choice == '3':
      print("Thank you for using the Application.")
      break
    else:
      print("Invalid choice. Please try again.")

    time.sleep(5)
if __name__ == "__main__":
  main()