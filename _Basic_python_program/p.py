n=int(input("Enter n:"))
for i in range (1,n+1):
    s=0
    for j in range (1,i//2+1):
        if i%j==0:
            s=s+j
    if i==s:
        print(i,"is perfect")
