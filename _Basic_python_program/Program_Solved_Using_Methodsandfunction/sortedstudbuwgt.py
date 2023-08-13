class Stud:
    def __init__(self,sno,name,wgt):
        self.sno=sno
        self.name=name
        self.wgt=wgt
    def __str__(self):
        return str(self.sno)+"\t"+(self.name)+"\t"+str(self.wgt)

                
        




s=[]
n=int(input("enter n"))
for i in range(n):
    sno=int(input("enter sno:"))
    name=input("enter name:")
    wgt=float(input("enter weight:"))
    s.append(Stud(sno,name,wgt))
s.sort(key=lambda x:x.wgt)

for i in s:
    print(i)

