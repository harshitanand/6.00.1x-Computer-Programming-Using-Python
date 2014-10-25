#this program describes the way of finding the root of polynomial
# of type (x^2 - y) where y is the number entered by user

#--------------------------------#
#---------Newton raphson---------#
#--------------------------------#

x = float(raw_input("Enter the value of number : "))

epsilon = .01
numGuess = 0
ans = x/2.0

while abs(ans**2-x) >= epsilon:
    ans = ans - ((ans**2 - x)/(2*ans))
    numGuess+=1
    print "The Guess is " + str(ans)
print "The number of Guess is " + str(numGuess)
print "The sqroot of " + str(x) + " is " + str(ans)
