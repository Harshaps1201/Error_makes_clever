class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("sum:",self.num1+self.num2)
    def sub(self):
        print("diff:",self.num1-self.num2)
    def mul(self):
        print("mul:",self.num1*self.num2)
    def div(self):
        print("div",self.num1/self.num2)
obj=calculator(10,2)
obj.add()
obj.sub()
obj.mul()
obj.div()