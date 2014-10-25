x = int(raw_input("Enter a number : "))

epsilon = 0.01
step = epsilon**2
ans = 0.0
guess = 0.0

while abs(ans**2-x)>=epsilon and abs(ans**2)!=x :
    ans = ans + step
    guess = guess+1
if abs(ans**2-x)>=epsilon :
    print "We could not find sq root of " + str(x)
else:
    print "The sq root of " + str(x) + "is " + str(ans)
