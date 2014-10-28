lowest_bal = 10
balance = 3329
annualInterestRate = 0.2

while(True):
    bal = balance
    for i in range(0,12):
        bal = (bal - lowest_bal) * (1+annualInterestRate/12.0)
    if bal <= 0:
        print "Lowest Payment : "+ str(lowest_bal)
        break
    else:
        lowest_bal += 10
