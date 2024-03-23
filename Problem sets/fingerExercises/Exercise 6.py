# Finger exercise: Let s be a string that contains a sequence of decimal numbers
# separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the
# sum of the numbers in s.

#attempt 1

# s = "1.23,2.3,3.123,8.12"
# separate = ""
# finalSum = 0.0

# for x in s:
#     separate += x
    
#     if x == ",":
#         separate = separate[:-1]
#         finalSum += float(separate)
#         separate = ""  
        
# finalSum += float(separate)  
# print(finalSum) 


#attempt2


# # could use split method

# s = "1.23,2.3,3.123,8.12"

# # Split the string into a list of substrings using a comma as the boundary
# values = s.split(",")

# finalSum = 0.0

# for value in values:
#     finalSum += float(value)

# print(finalSum)
    

#attempt 3


s = "1.23,2.3,3.123,8.12"

# Split the string into a list of substrings using a comma as the delimiter
values = s.split(",")

# Use a list comprehension to convert the substrings to floats and sum them
finalSum = sum(float(value) for value in values)

print(finalSum)
