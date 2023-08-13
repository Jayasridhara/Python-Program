
def sum(n):
    if(n<10):
        return n
        
    s=0
    while(n!=0):
        r=n%10
        s+=r
        n=n//10
    return ssum(s)
  
n=int(input("enter n:"))
result=sum(n)
print(result)
