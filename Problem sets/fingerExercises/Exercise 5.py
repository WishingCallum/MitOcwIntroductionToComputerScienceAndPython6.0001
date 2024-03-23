# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:41:29 2023

@author: CallumD
"""

# Write a program that asks the user to enter an integer and prints
# two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists,
# it should print a message to that effect.

x = int(input('Enter an integer: ')) 
pwr = 1
root = 2
toomanytries = False
while toomanytries == False:
    pwr += 1 # power can be 2 as there is no integer root of 1 or 2
    
    if root ** pwr == x: 
            print("The root is " , root)
            print("The power is " , pwr)
            print(root , "**" , pwr , "=" , x)
            break
    elif pwr > 5 :
            root += 1
            pwr = 1
    elif root > x:
        print ("there is no integer root function for " , x)
        break # can make toomanytries false but break just ends the program


## very proud of this one even if it is simple
# this felt veeery rewarding to build
#you could make another list that stored the results of root ** pwr and if all of them > x could break