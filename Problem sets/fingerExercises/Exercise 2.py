x = 12
y = 23
z = 42
highestOdd = 0

if (x % 2) != 0:  #all odd numbers arent divisible by 2. The expression x % 2 will create a float within the memory
    highestOdd = x

if (y & 2) != 0:
    highestOdd = y

if (z % 2) != 0:
    highestOdd = z

if highestOdd == 0:
    print("There were no odd values")
else:
    print("The highest odd number was " + str(highestOdd))