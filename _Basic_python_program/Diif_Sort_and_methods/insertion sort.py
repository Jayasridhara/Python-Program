l=[2,3,4,5,7,8,9,6,4]
for i in l:
    j=l.index(i)
    while j>0:
        if l[j-1]>l[j]:
            l[j-1],l[j]=l[j],l[j-1]
        else:
            break
        j=j-1
print(l)
