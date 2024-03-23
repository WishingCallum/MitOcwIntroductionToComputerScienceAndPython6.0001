annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home:"))
semi_anual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = 0.25
r = 0.04

def numOfMonths(annual_salary, total_cost, portion_down_payment, portion_saved, r, semi_anual_raise):
    current_savings = 0
    months = 0
    while current_savings < total_cost * portion_down_payment:
        current_savings += (annual_salary/12) * portion_saved #add the portion saved this month
        months +=1
        
        if months % 6 == 0: #if divisible by 6 after the 6th month (will effect only 7th onwards)
            annual_salary += annual_salary * semi_anual_raise
            
        if months % 12 == 0:
            current_savings += (current_savings *r) #roi yearly
            
    return months
    
print("Number of months:" , numOfMonths(annual_salary, total_cost, portion_down_payment, portion_saved, r, semi_anual_raise))    
