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
    def scal(self,k):
        return Point(self.x*k,self.y*k)
    def norm(self):
        return Point(self.y, -self.x)