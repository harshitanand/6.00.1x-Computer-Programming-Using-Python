x = int(raw_input("Enter a number: "))
ans = 0
while ans**3 < abs(x) :
    ans = ans + 1
if ans**3 == abs(x):
    if x < 0:
        ans = -ans
    print " Cube root of "+ str(x) +" is " + str(ans)
else:
    print " Cube root does not exists "
