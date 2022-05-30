class A:
    def __init__(self,val):
        self.val=val
    def __add__(self,other):
        if type(other)==type(self):
            self.val+=other.val
        else:
            self.val+=other

a=A(1)
print(a.val)
b=A(2)
print(b.val)
a+b
print(a.val)
a+1
print(a.val)
