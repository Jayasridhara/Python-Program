a="developer"
b="fresher"
l=[]

for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            a=a.replace(a[i],"#")
            b=b.replace(b[j],"#")
            break
c=list(a+b)
for i in c:
    if(i.isalpha()):
        l.append(i)
print(l)

    
    
    
