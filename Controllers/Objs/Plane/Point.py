class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def ro(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def __mul__(self, other):
        return self.x*other.x+self.y*other.y
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def norm(self):
        return Point(self.y, -self.x)
    def abs(self):
        return ((self.x)**2+(self.y)**2)**0.5
    def copy(self):
        return Point(self.x,self.y)