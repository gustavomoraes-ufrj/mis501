#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:06:39 2024

@author: gustavo
"""

A = [1,3,10,11]

# def is_valid_index(st, index):
#     return 0 <= index < len(st)

def is_valid_index(s, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    return -len(s) <= index < len(s)

def askIndex(s):
    pos = input("Enter the index: ")
    intPos = int(pos)
    val = input("Enter the value: ")
    
    if not is_valid_index(s, intPos):
        print("Index not valid")
        print("Please, try again!")
        return False
    else:
        s[intPos] = val
        return True

while True:
    if askIndex(A):
        break

print("End of program")
print(A)
