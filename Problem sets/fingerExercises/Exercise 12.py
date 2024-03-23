# def findnums(s):
#     returnvalue = ""
#     for i in s:
#         if i.isdigit():
#             returnvalue += i
#     return returnvalue
            


# string = "ab24bad4"
# print (findnums(string))

def findnums(s):
    returnvalue = ''
    for i in s:
        try:
            
            returnvalue += int(i)
            pass
        except:
            pass
            
    return returnvalue
            


string = "ab24bad4"
print (findnums(string))