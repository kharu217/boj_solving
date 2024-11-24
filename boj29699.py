n = int(input())
s = 'WelcomeToSMUPC'

if n <= len(s) :
    print(s[n-1])
else :
    temp =len(s)%n
    print(s[n%len(s)-1])
