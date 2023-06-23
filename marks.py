t=int(input("enter tamil mark:"))
e=int(input("enter english mark:"))
m=int(input("enter maths mark:"))
sci=int(input("enter science mark:"))
soc=int(input("enter social science mark:"))
tot=t+e+m+sci+soc
if(tot<100):
    print("p grade")
elif(tot<=200):
    print("m grade")
elif(tot<300):
    print("i grade")
elif(tot<=400):
    print("s grade")
else:
    print("t grade")
    
