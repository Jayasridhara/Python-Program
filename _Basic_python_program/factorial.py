n=int(input("enter n"))
a=-1
b=1
for i in range(n):
    c=a+b
    print(c,"\t")
    a=b
    b=c
