#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:27:28 2024

@author: gustavo
"""

A = [1,3,10,11,16]

# def is_valid_index(st, index):
#     return 0 <= index < len(st)

def is_valid_index(s, index):
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    return -len(s) <= index < len(s)

def askIndex():
    pos = input("Enter the index: ")
    intPos = int(pos)
    
    if not is_valid_index(A, intPos):
        print("Index not valid")
        print("Please, try again!")
        return False
    else:
        print(A[intPos])
        return True

while True:
    if askIndex():
        break

print("End of program")
print(len(A))
print(-len(A))