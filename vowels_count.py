vowels_count = 0
s = str(raw_input("Enter the String : "))

for i in range(len(s)):
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
        vowels_count+=1

print "The number of vowels in " + str(s) + " is " + str(vowels_count)
