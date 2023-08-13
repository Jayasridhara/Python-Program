l=[]
t=[]
s=0
a="c2i2tr!is0y!1s"
for i in a:
    if(i.upper()>='A' and i.upper()<='Z'):
        l.append(i)
    elif(i>='0' and i<='9'):
        s+=int(i)
    else:
        t.append(i)
l.append(str(s))
l.extend(t)
print(''.join(l))
        
