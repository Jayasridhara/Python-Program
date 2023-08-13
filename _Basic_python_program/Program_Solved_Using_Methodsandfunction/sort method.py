class Stud:
    def __init__(self,sno,name,wt):
        self.sno=sno
        self.name=name
        self.wt=wt
    def __str__(self):
        return 'f{self.sno}\t{self.name}\t{self.wt}'
    
if __name__=="___main__":
    s=[]
    
    s1=Stud(23,"thara",45.6)
    s2=Stud(45,"simren",67.8)
    s3=Stud(67,"kiren",64.8)
    s4=Stud(45,"nayan",89.8)
    s.append(s1)
    s.append(s2)
    s.append(s3)
    s.append(s4)
    k=sorted(key=lambda x:x.wt)
    for i in k:
        print(i)

        
