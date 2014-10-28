balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthly_interest_rate = annualInterestRate/12.0
Rb = 0.0
ub = 0.0
monthly_payment=0.0
tot_paid=0.0

for i in range(0,12):
    monthly_payment = round(monthlyPaymentRate*balance,2)
    ub = round(balance - monthly_payment,2)
    Rb = round(ub + (monthly_interest_rate)*ub,2)
    balance = Rb
    tot_paid = round(tot_paid + monthly_payment,2)
    print "Month: "+ str(i)
    print "Minimum monthly payment: "+ str(monthly_payment)
    print "Remaining balance: "+ str(Rb)

print "Total paid: "+ str(tot_paid)
print "Remaining balance: "+ str(Rb)
    
