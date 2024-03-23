# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:38:48 2023

@author: CallumD
"""

# Write a program that asks the user to input 10 integers, and then
# prints the largest odd number that was entered. If no odd number was entered, it
# should print a message to that effect.
x = 0
listofnums = [None] * 10 # this is how you define an empty list for x ammount you can do 
#listofnume = [] though you have to use the append method (method is passed into an object)
#
biggestOddnum = 0

while x < 10:
    listofnums[x] = int(input("please enter an integer, this is number " + str(x+1) + " ")) #you need to cconcatonate input
    
    if listofnums[x]&2 == 0:# this operator % converts the integer into binary AND operator between the 2 integers
            if listofnums[x] > biggestOddnum:
                biggestOddnum = listofnums[x]
    x += 1        
           
        

if biggestOddnum == 0:
    print("There was no largest odd number")
else:
    print("The biggest odd number was " , biggestOddnum)
   