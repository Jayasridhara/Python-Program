n=int(input("enter n:"))
t=n%10
n=n//10
s=0
while(n!=0):
    r=n%10
    s=s+2*r
    n=n//10
if(s//4==t):
    print("success")
else:
    print("not success")
    
