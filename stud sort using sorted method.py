class Student:
    def __init__(self,sno,name,wt):
        self.sno=sno
        self.name=name
        self.wt=wt
    def __str__(self):
        return f'{self.sno}\t{self.name}\t{self.wt}'
def fun(e):
        return e.wt
  

l=[]
n=int(input("enter n:"))
for i in range(1,n+1):
    sno=int(input("enter sno:"))
    name=input("enter name")
    wt=float(input("enter wt:"))
    l.append(Student(sno,name,wt))
k=sorted(l,key=fun)

for i in k:
    print(i)
