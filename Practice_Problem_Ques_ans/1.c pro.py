s="hello"
l=[]
for i in s:
    if(ord(i)>=97 and ord(i)<=122):
        l.append(chr(ord(i)-32))
print(''.join(l))
        
