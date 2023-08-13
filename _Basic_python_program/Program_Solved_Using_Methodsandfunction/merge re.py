s='areyfdgfh'
r='denim'
n=3
m=5
l=[]
k=[]
n=min(len(s),len(r))


for i in range(n):
    l.append(chr(min(ord(s[i]),ord(r[i]))))
    k.append(chr(max(ord(s[i]),ord(r[i]))))
k=k[::-1]
if len(r)>len(s):
    
    for i in range(n,len(r)):
        l.append(r[i])
    l.extend(k)
    print(' '.join(l))
else:
    for i in range(n,len(s)):
        l.append(s[i])
    l.extend(k)
    print(' '.join(l))
    
       
