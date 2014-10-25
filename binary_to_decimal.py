num = int (raw_input("Enter a number to convert: "))

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = result + str(num%2)
    num = num/2
if isNeg:
    result = '-' + result
