balance = 320000
annualInterestRate = 0.2
monthlyInterestRate =annualInterestRate/12.0
lb = balance/12
ub = (balance*(1+monthlyInterestRate)**12)/12.0
lowest_payment = (lb+ub)/2.0
numGuess = 0
epsilon = 0.01
bal = balance

while abs(bal) >= epsilon:
    bal = balance
    for i in range(12):
        numGuess += 1
        bal = (bal - lowest_payment) * (1+monthlyInterestRate)
    if bal==0.0:
        break
    elif bal > 0.0:
        lb = lowest_payment
    else:
        ub = lowest_payment
    lowest_payment = (lb+ub)/2.0
lowest_payment = round(lowest_payment,2)
print "This total Guess are "+ str(numGuess)
print "Lowest Payment: "+ str(lowest_payment)
