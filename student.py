class Student:
    def __init__(self,sno,name,regno,wgt):
        self.sno=sno
        self.name=name
        self.regno=regno
        self.wgt=wgt
    def __str__(self):
        return f'{self.sno}\t{self.name}\t{self.regno}\t{self.wgt}'









s=[]
n=int(input("enter n:"))
for i in range(n):
    sno=int(input("enter sno"))
    name=input("enter name")
    regno=int(input("enter regno:"))
    wgt=float(input("enter wgt:"))
    s.append(Student(sno,name,regno,wgt))
for i in range(n-1):
    for j in range(i+1,n):
        if(s[i].wgt!=s[j].wgt):
            s.sort(key=lambda x:x.wgt)
        elif(s[i].name!=s[j].name):
            s.sort(key=lambda x:x.name)
        elif(s[i].regno!=s[j].regno):
            s.sort(key=lambda x:x.regno)
        else:
            s.sort(key=lambda x:x.sno)
            
            
    
    
for i in s:
    print(i)

