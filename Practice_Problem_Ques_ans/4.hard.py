a=[]
b=["fizz"]
c=["buzz"]
d=["fizz buzz"]
for i in range(1,101):
    if i%5==0 and i%7==0:
        a.append(d[0])
    elif i%5==0 and i<=50:
         a.append(b[0])
    elif i%7==0 and i>=50:
        a.append(c[0])
    else:
        a.append(i)
for k in a:
    print(k,end=' ')
