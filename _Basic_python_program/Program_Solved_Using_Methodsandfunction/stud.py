class Stud:
    def __init__(self,sno,name,wt):
        self.sno=sno
        self.name=name
        self.wt=wt
    def __str__(self):
        return str(self.sno)+'\t'+self.name+'\t'+str(self.wt)
    
if __name__ == '__main__':
    
    s=[]
    s1=Stud(23,"thara",45.6)
    s2=Stud(45,"simren",67.8)
    s3=Stud(67,"kiren",64.8)
    s4=Stud(45,"nayan",89.8)
    s.append(s1)
    s.append(s2)
    s.append(s3)
    s.append(s4)
    s.sort(key=lambda x : x.wt)
    for i in s:
        print(i)

        
#s.sort(key=lambda x:x.wt)
