# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 09:34:43 2023

@author: CallumD
"""
#Finding the cost of a downpayment on a house

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home:"))

portion_down_payment = 0.25
r = 0.04
months = 0
def numOfMonths(total_cost, portion_down_payment, months, portion_saved, r):
    current_savings = 0
    while current_savings < total_cost * portion_down_payment:
        months += 1
        current_savings += (annual_salary/12) * portion_saved #add the portion saved this month
    
        if months % 12 == 0:
            current_savings += (current_savings *r) #roi yearly
        
    return months
    
print("Number of months:" , numOfMonths(total_cost, portion_down_payment, months, portion_saved, r))    

