n=int(input("enter n:"))
s=0
if n>=1 and n<=100:
    for i in range(1,n//2+1):
        if(n%i==0):
            s+=i
    if(s==n):
        print(n,"is perfect")
    else:
        print(n,"not perfect")
else:
    print("not in range")
    
    
