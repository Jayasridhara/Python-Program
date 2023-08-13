s=input("enter n:")
#yusing dict
'''d={}
for i in a:
    d[i]=d.get(i,0)+1
#print(d)
for i,j in d.items():
    print(i,"--->",j)
'''
# using list
k=set(s)
for i in k:
    f=s.count(i)
    print(i,"--->",f)
