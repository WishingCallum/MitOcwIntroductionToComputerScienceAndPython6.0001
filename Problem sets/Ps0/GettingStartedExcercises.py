# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:38:02 2023

@author: CallumD
"""

# exercise 1
print (6+4*10)

# exercise 2
print ((6+4)*10)

#python follows bodmas opperations, solve the brackets
#orders is to the power of or square roots
#division and multiplication happen at the same time
#same with addition and multiplication


# print(8/2*(2+2))  

# with bodmas this will get the awnser 16
#eventually the program gets to 8 / 2 *(4)
#in bodmas if the same percendece occures we do our calculations right to left
#which gives us 8/2= 4      4(4)
#it will also give us a float because we are dividing!

# print(8/(2*(2+2)))

#however in this example because of the order of the brackets
#the program specifies it has to simplify the brackets before dividing the numbers
#outside of the brackets


#exercise 3
print(23.0**5)


#exercise 4 
 
#find the positive root of the quadratic equation 34*x^2 + 68*x - 510 

#the quadratic formuala can take the form of  a*x^2 + b*x + c = 0



#If there were only 2 terms instead of 3 we would "find the difference of squares"
#(x+2)(x-2)



# probably worth revising some higher maths, this uses the quadratic equasion

#        -b ± sqrt(b**2−4*a*c)
#  X = _________________________
#                2a
 
 #a = 34     b = 68     c = -510
 



a = 34
b = 68
c = -510


rootpos = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
rootneg = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print("the positive root is", rootpos)
print("the negative root is", rootneg)

#exercise 5
import math
print(math.cos(3.4)**2+math.sin(3.4)**2)

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# result = fibonacci(7)                           

#                                           index start at 0  1  2  3  4  5  6  7
# print(result)  # This will print 13 (Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13)

