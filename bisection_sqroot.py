x = float (raw_input("Enter the value : "))

epsilon = .01
numGuess = 0
low = 0.0
high = x

ans = (low+high)/2

while abs(ans**2-x) >= epsilon:
    print "low=" + str(low) + " high=" + str(high) + " ans=" + str(ans)
    numGuess+=1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (low+high)/2
print "number of guesses is " + str(numGuess)
print "The sq root of " + str(x) + " is " + str(ans)
