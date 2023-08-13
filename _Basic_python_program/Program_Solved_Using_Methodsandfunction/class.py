class Add:
    def __init__(self):
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))
    '''def input(self):
        self.a=int(input("enter a:"))
        self.b=int(input("enter b:"))'''
    def process(self):
        self.c=self.a+self.b
    '''def output(self):
        print(self.c)'''
    def __str__(self):
        return str(self.c)

if __name__=="__main__":
    a=Add()
    #a.input()
    a.process()
    #a.output()
print(a)
