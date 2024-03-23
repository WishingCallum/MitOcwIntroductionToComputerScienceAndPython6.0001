# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 10:51:53 2023

@author: CallumD
"""
# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.

x = input("Enter number x: ")
y = float(input("Enter number y: "))
print("X**y = ", int(x)**int(y))

#log base 2(16) = 4
#there will be float numbers in this
# we will have to do exauhstive enumeration
# we will find the root lower than when root > x
# we will find which decimal root of 1 and 9 is closer for 20 digets



#the sheet told us to use numpy or pylab to figure out log(x), however I think
#as a test of what ive lerned so far id like to do all of the calcualtions without imports like decimal or numpy

#I think this will challenge me a lot more and I will be able to use more of the things ive
#learnt so far. This will make me think more




# if my  2 **  current value is closer to x than my current best value
# and 2 ** current value < x 
# we have found a closer match


#first we should loop to see which one of 2^x is closest

xFloat = float(x)
pwr = 1.0


#the first pwr will need to use exauhstive inumeration as we dont know how big x will be , calculating this seperate from the rest of 
# the decimal power digets will save compute

def Findpwr(xFloat, pwr):
    pwr +=1
    if 2 ** pwr == xFloat: ##swap 2** pwr if you need the 100 error
        return pwr
    
    elif 2 ** pwr > xFloat:
        pwr -= 1.0
        return pwr
        
    else: return Findpwr(xFloat, pwr)

# tried itterating 0.00000000001 units at a time but floating point rounding errors
#going to have to do some casting 

bestPwr = Findpwr(xFloat, pwr)
pwrDecimal = bestPwr
pwrDecimal_str = str(pwrDecimal)  # Convert to string
bestValue = 0
bestValue_str = str(bestPwr)
counter = -1
finalProduct = '0'
decimalPoint = 0
decimalPoint = bestValue_str.index('.')
if 2 ** bestValue != xFloat:
    strlist = list(pwrDecimal_str) #4,.,0
    output_string = ''.join(strlist) #4.0 str


    while counter != -20 :
            
            
            
           
               
        
            def removeDecimal(strlist): #takes list and turns it into a string
                
                del strlist[decimalPoint] #remove decimal from the list [4,0]
                output_string = ''.join(strlist) #40
                
                return(output_string)
            
            
            def intplusone(input_string):    #takes string turns into a list
                plusOne = int(input_string) #cast to int 40
                plusOne += 1 #41
                input_string = list(str(plusOne)) #cast to list again [4,1]
                return input_string
                
            def addDecimal(input_list):                                    #takes list and turns into a string
                input_list.insert(decimalPoint, '.') #re add recimal [4,.,1]
                output_string = ''.join(input_list) #make the list a string (4.1) as you cant cast float to a list
                return  output_string
            
            
                
                
            removeDecimalFromList = removeDecimal(strlist) #4.1 to 41
            
            addOneToInteger = intplusone(removeDecimalFromList) # 41 to 42
            
            finalProduct = addDecimal(addOneToInteger)#42 to 4.2
            
            
            strlist = list(str(finalProduct)) # we need to pass the result back into the remove decimal from list after the loop
            
            
              
        
            if 2 ** float(finalProduct) > 2 ** bestValue and (2 ** float(finalProduct)) < xFloat:
                    
                    bestValue = float(finalProduct)
                    bestValue_str = str(bestValue)
                    
            if strlist[-1] == '9': #last decimal place is 9 
                
                # if bestValue_str != pwrDecimal_str:
                    strlist = list(bestValue_str) #4.7
                    del strlist[decimalPoint] #remove char '.'
                    strlist.append('0') # 47 to 470
                    strlist.insert(decimalPoint, '.') #re add recimal [4,.,7,0]
                    counter -= 1
                # elif bestValue_str == pwrDecimal_str:
                #     del strlist[decimalPoint] #remove char '.'
                #     strlist.append('0') # 47 to 470
                #     strlist.insert(decimalPoint, '.') #re add recimal [4,.,7,0]   THE REASON THIS CODE EXISTS THAT THE CODE ASSUMES A BEST VALUE WILL BE FOUND
                #BY 2 DECIMAL POINTS
                # TP SEE THIS ERROR PWR ** 2
                
                #     counter -= 1
                    
                #     strlist.append()
                
                        
                            
            
print('log(x) = ' + bestValue_str)                        
                        
                

