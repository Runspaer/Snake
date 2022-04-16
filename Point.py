import numpy as np
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





    ##Попытка реализации алгоритма
    def FindFurthestPoint(self,pointers: list):#r pointers
        r=Point(self.x,self.y)
        max_point = 0
        max_r = -100000000000000000000
        for i in pointers:
            if i * r > max_r:
                max_r = i * r
                max_point = i
        return max_point

    def Support(self,A, B):#r A B
        r=Point(-self.x,-self.y)
        return self.FindFurthestPoint(A) - r.FindFurthestPoint(B)

    def GJK(self,A, B):#self по факту мусор, так что эту функцию надо поместить где-нибудь повыше, можно даже в enjune
        support = Point(1, 0).Support(A, B)
        Simplex = []
        Simplex.append(support)
        direction = Point(-support.x, -support.y)
        while direction:
            support = direction.Support(A, B)
            if support * direction <= 0:
                return False
            Simplex.append(1)#Ничего не обозначает и добавлено для удобства вставки в начало
            for i in range(len(Simplex)):
                if i != len(Simplex) - 1:
                    Simplex[-i], Simplex[-i - 1] = Simplex[-i - 1], Simplex[-i]
                else:
                    Simplex[0] = support
            direction=self.CalculateDirection(Simplex)
        return True#new Collision(a, b);

    def CalculateDirection(self,Simplex):#self по факту мусор, так что эту функцию надо поместить где-нибудь повыше, можно даже в enjune
        a=Simplex[-1]
        ao=Point(-a.x,-a.y)
        if len(Simplex)==3:#Треугольник
            b=Simplex[1]
            c=Simplex[0]
            ab=b-a
            ac=c-a
            abPerp=Point(ab.y,-ab.x)
            if abPerp*c>=0:
                abPerp=Point(-abPerp.x,-abPerp.y)
            if abPerp*ao>0:
                Simplex=Simplex[:1]
                return abPerp
            acPerp=Point(ac.y,-ac.x)
            if acPerp*b>=0:
                acPerp=Point(-acPerp.x,-abPerp.y)
            if acPerp*ao>0:
                Simplex=Simplex[1:1]
                return acPerp
            return 0
        #Не треугольник,т.е. линия
        b=Simplex[0]
        ab=b-a
        abPerp=Point(ab.y,-ab.x)
        if abPerp*ao<=0:
            abPerp=Point(-abPerp.x,-abPerp.y)
        return abPerp
    # def NextSimplex(self,Simplex):# direction=self
    #     direction=Point(self.x,self.y)
    #     if len(Simplex) == 2:
    #         return direction.Line(Simplex)
    #     else:
    #         return direction.Triangle(Simplex)
    #
    # def Samedirection(self, other):
    #     return self * other > 0
    # def Line(self,Simple):# direction=self
    #     direction=Point(self.x,self.y)
    #     a = Simple[0]
    #     b = Simple[1]
    #     ab = b - a
    #     ao = Point(0, 0) - a
    #     if ao.Samedirection(ab):
    #         direction.x, direction.y = np.cross([np.cross([ab.x, ab.y], [ao.x, ao.y])[0], np.cross([ab.x, ab.y], [ao.x, ao.y])[1]], [[ab.x, ab.y]])
    #     else:
    #         Simple = [a]
    #         direction = ao
    #     return False
    #
    #
    #
    # def GJK(self,A, B):#self по факту мусор, так что эту функцию надо поместить где-нибудь повыше, можно даже в enjune
    #     support = Point(1, 0).Support(A, B)
    #     Simplex = []
    #     Simplex.append(support)
    #     direction = Point(-support.x, -support.y)
    #     while True:
    #         support = Support(A, B, direction)
    #         if support * direction <= 0:
    #             return False
    #         Simplex.append(1)
    #         for i in range(len(Simplex)):
    #             if i != len(Simplex) - 1:
    #                 Simplex[-i], Simplex[-i - 1] = Simplex[-i - 1], Simplex[-i]
    #             else:
    #                 Simplex[0] = support
    #         if NextSimplex(Simplex, direction):
    #             return True

A = [Point(1, 1), Point(3, 2), Point(5,1)]
B = [Point(5, 1), Point(8, 2), Point(10,1)]
p=Point(1,1)
print(p.GJK(A,B))