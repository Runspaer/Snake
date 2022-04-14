class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def ro(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5