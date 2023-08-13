a="a1000b3"
l=[]
p=[]
n=0
for i in a:
    if i.isalpha():
        p.append(n*l)
        l.clear()
        l.append(i)
        n=0
    else:
        n=n*10+int(i)
p.append(n*l)
print(sum(p,[]))
