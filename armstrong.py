n=int(input("enter n:"))
a=len(str(n))
temp=n
rev=0
while(n>0):
    r=n%10
    rev=rev+(r**a)
    n=n//10
if temp==rev:
    print("armstrong")
else:
    print("not armstrong")
