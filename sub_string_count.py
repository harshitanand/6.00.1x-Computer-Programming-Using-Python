sub_string_count = 0
s = str(raw_input("Enter the string : "))

for i in range(len(s)):
    if s[i:i+3] == 'bob':
        sub_string_count+=1

print "The no. of Substrings present in "+ str(s) + \
      " is "+ str(sub_string_count)
