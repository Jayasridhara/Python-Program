def fun(m,n,p):
    if(m==0 and n!=0):
        print(a[n],end=' ')
    elif(m==1 and n!=0):
        print(b[n],end=' ')
    elif(m!=0 and n==0):
        print(c[m],end=' ')
    else:
        print(c[m],a[n],end=' ')
    if(m!=0 or n!=0):
        print(d[p],end=' ')


a=['','one','two','three','four','five','six','seven','eight','nine']
b=['','eleven','tweleve','thirteeen','fourteen','fifteeen','sixteeen','seventeen','eighteen','ninteeen']
c=['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
d=['','crore','lakhs','thousand','hundred']



l=[]
n=int(input("enter n"))
if n>=100:
    print("out of range")
else:
    i=0
    while n!=0:
        l.append(n%10)
        n=n//10
        i=i+1
    for k in range(i,9):
        l.append(0)
    fun(l[8],l[7],1)
    fun(l[6],l[5],2)
    fun(l[4],l[3],3)
    fun(0,l[2],4)
    fun(l[1],l[0],0)
