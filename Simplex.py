from Point import *
class Simplex:
    def __init__(self, l:list):
        self.l=l

    def CalculateDirection(self):
        #for i in range(len(self.l)):
        #    print(self.l[i].x,self.l[i].y)
        #print()
        a = self.l[-1]
        ao = Point(-a.x, -a.y)
        if len(self.l) == 3:  # Треугольник
            b = self.l[1]
            c = self.l[0]
            ab = b - a
            ac = c - a
            abPerp = Point(ab.y, -ab.x)
            if abPerp * c >= 0:
                abPerp = Point(-abPerp.x, -abPerp.y)
            if abPerp * ao > 0:
                self.l = self.l[:1]
                return abPerp
            acPerp = Point(ac.y, -ac.x)
            if acPerp * b >= 0:
                acPerp = Point(-acPerp.x, -abPerp.y)
            if acPerp * ao > 0:
                self.l = self.l[1:1]
                return acPerp
            return False
        # Не треугольник,т.е. линия
        b = self.l[0]
        ab = b - a
        abPerp = Point(ab.y, -ab.x)
        if abPerp * ao <= 0:
            abPerp = Point(-abPerp.x, -abPerp.y)
        return abPerp
    def push_back(self,i: Point):
        self.l.append(i)
