n=int(input("enter n:"))
def fun(n):
    s=0
    n=list(str((n)))
    for i in n:
        s=s+int(i)
    n=s
      
while(n>9):
    fun(n)

print(n)
    
    
    
