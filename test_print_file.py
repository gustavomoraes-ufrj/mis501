#!/usr/bin/python3

import sys

# Define the file path where you want to save the output
file_path = 'output.txt'

# Redirect the output to the file
with open(file_path, 'w') as f:
    sys.stdout = f
    print('Hello, world!')

# Reset sys.stdout to its original value
sys.stdout = sys.__stdout__