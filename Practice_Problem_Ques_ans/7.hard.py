import math
def prime(l):
    f=1
    for i in range(3,math.isqrt(l),2):
        if l%i==0:
            f=0
            break
        return f
    
n=int(input("enter n:"))
l=int(math.pow(2,n)+1)

if prime(l)==2:
    print(l,"prime")
    
else:
    for i in range(1,(l//2)+1):
        if l%i==0:
            print(i)
    print("Hi")
    print(l)
    print("Hello")
    
