n=int(input("Enter a no."))
temp=n
rev=0
d=0
while temp>0:
    d=temp%10
    rev=rev*10+d
    temp//=10
if n==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
    