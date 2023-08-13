a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=int(input("Enter d:"))
e=int(input("Enter e:"))
f=int(input("Enter f:"))
if a>b and a>c and a>d and a>e and a>f:
    print(a,"is greatest")
elif b>c and b>d and b>e and b>f:
    print(b,"is greatest")
elif c>d and c>e and c>f:
     print(c,"is greatest")
elif d>e and d>f:
    print(d,"is greatest")
elif e>f:
    print(e,"is greatest")
else:
    print(f,"is graetest")
    
