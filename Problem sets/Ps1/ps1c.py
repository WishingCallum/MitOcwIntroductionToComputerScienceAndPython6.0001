# -*- coding: utf-8 -*-
"""
You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
the required down payment. 

In ps1c.py, write a program to calculate the best savings rate, as a function of your starting salary.
You should use bisection search to help you do this efficiently. You should keep track of the number of 
steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote
for part B in this problem.  

Because we are searching for a value that is in principle a float, we are going to limit ourselves to two
decimals of accuracy (i.e., we may want to save at 7.04% ­­ or 0.0704 in decimal – but we are not 
going to worry about the difference between 7.041% and 7.039%).  This means we can search for an
integer between 0 and 10000 (using integer division), and then convert it to a decimal percentage
(using float division) to use when we are calculating the current_savings after 36 months. By using
this range, there are only a finite number of numbers that we are searching over, as opposed to the
infinite number of decimals between 0 and 1. This range will help prevent infinite loops. The reason we
use 0 to 10000 is to account for two additional decimal places in the range 0% to 100%. Your code
should print out a decimal (e.g. 0.0704 for 7.04%).

"""
#
annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_anual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
current_savings = 0
#num of months variables 

numGuesses =0
int_max_guess =10000
int_min_guess = 1
portion_saved = int((int_max_guess + int_min_guess)/2.0) 


def numOfMonths(annual_salary, total_cost, portion_down_payment, portion_saved, r, semi_anual_raise):
    current_savings = 0
    months = 0
    while months < 36 :
        current_savings += (annual_salary/12) * portion_saved #add the portion saved this month
    
        months +=1
        if months % 6 == 0: #if divisible by 6 after the 6th month (will effect only 7th onwards)
            annual_salary += annual_salary * semi_anual_raise
            
        if months % 12 == 0:
            current_savings += (current_savings *r) #roi yearly
            
    return current_savings

while total_cost*portion_down_payment - current_savings > 100 or total_cost*portion_down_payment - current_savings < -100: # within 100
    current_savings = numOfMonths(annual_salary, total_cost, portion_down_payment, float(portion_saved)/10000, r, semi_anual_raise) #passes in the guess as a float /10000 so it becomes a decimal
    numGuesses += 1
    if current_savings < total_cost*portion_down_payment  : # less than 250k
        
        int_min_guess = int(portion_saved)
                            
    else:
        
        int_max_guess = int(portion_saved)
        
    portion_saved = int((int_max_guess + int_min_guess)/2.0) 
    if int_min_guess > 9998:
        
        break

if int_min_guess > 9998:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate =", float(portion_saved)/10000)
    print("Steps in bisection search:", numGuesses)