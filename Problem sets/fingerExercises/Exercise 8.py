
#change high to just be x, max always finds the highest value so it always goes to 1 for positive
#abs is necesarry for the negative comparisons to work
#ans**3 as cube root
#low does not have to be changed

x = -150
epsilon = 0.01 # has to be at least this close
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
   
while abs(ans**3 - x) >= epsilon: 
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if abs(ans**3) < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
        
print('numGuesses =', numGuesses)
print(ans, 'is close to cube root of', x)
