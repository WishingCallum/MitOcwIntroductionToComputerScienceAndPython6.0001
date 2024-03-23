# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:34:47 2023

@author: CallumD
"""

# Finger exercise: Write a function isIn that accepts two strings as arguments and
# returns True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operation in.
string1 = 'find me'
string2 = "you'll never find me"

def findme(string1, string2):
    return string1 in string2

print(findme(string1, string2))