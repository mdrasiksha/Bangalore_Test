class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print("EmpId:{} EmpName:{} EmpSal:{}".format(self.eid,self.ename,self.sal))
        