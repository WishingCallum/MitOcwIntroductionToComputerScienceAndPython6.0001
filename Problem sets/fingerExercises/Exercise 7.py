# Finger exercise: What would the code in Figure 3.4 do if the statement x = 25
# were replaced by x = -25?

#abs always produces positive values so it will be the exact same result as 25

x = -25
epsilon = 0.01 # has to be at least this close
numGuesses = 0
low = min(-1,x)
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)