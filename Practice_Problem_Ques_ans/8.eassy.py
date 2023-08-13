n=int(input("enter n:"))
s=0
m=n
while n!=0:
    r=n%10
    s+=r
    n=n//10
if(3*s==m):
    print(m,"is equal")
else:
    print(m,"is not equal")
    
