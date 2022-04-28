from Objs.Plane.Simplex import *
from Objs.Geometry import *
import math as m

class Physics:
    def __init__(self,geom:Geometry):
        self.geom=geom
    def draw(self,screen):
        self.geom.draw(screen)
    def copy(self):
        return Physics(self.geom.copy())
    def give_clash_norm(self):
        pass
    def is_collision(self,other):
        return self.GJK(other)
    def clash(self,other):
        pass
    def find_furthest_point(self, direction:Point):
        pass
        # pointers=self.search_points()
        # max_point = Point(0,0)
        # max_r = -10000000000000000000
        # for i in pointers:
        #     if i * direction > max_r:
        #         max_r = i * direction
        #         max_point = i
        # return max_point

    def support(self, B, direction: Point):  # r A B #A B r
        return self.find_furthest_point(direction) - B.find_furthest_point(Point(-direction.x,-direction.y))#-r
    def GJK(self,B):
        support = self.support(B,Point(1,0))# r a b # a b r
        simplex=Simplex([support])
        #direction = Point(-support.x, -support.y)
        direction = Point(-1, 0)
        while direction:
            support = self.support(B, direction)
            # print(direction.x, direction.y)
            # print(support.x,support.y)
            # print()
            if support * direction <= 0:
                return False
            simplex.push_back(support)
            direction = simplex.CalculateDirection()
        return True


class Physics_circle(Physics):
    def find_furthest_point(self, direction:Point):
        angle=m.atan2(direction.y, direction.x)
        return Point(self.geom.center.x + (self.geom.peaks[0].abs() * m.cos(angle)),self.geom.center.y + (self.geom.peaks[0].abs() * m.sin(angle)))
    def copy(self):
        return Physics_circle(self.geom.copy())

class Physics_polygon(Physics):#на самом деле это плоский объект, сделано для упрощения, так как в дальнейшем процесс высчитывания будет иным
    def find_furthest_point(self, direction:Point):
        pointers=self.geom.give_gl_peaks()
        max_point = Point(0,0)
        max_r = -10000000000000000000
        for i in pointers:
            if i * direction > max_r:
                max_r = i * direction
                max_point = i
        return max_point
    def give_clash_norm(self):# в будущем можно будет находить вектор, где произошло стокновение и возвращать его
        return [(self.geom.give_gl_peaks()[0]-self.geom.give_gl_peaks()[1]).norm(),(self.geom.give_gl_peaks()[1]-self.geom.give_gl_peaks()[0]).norm()]
        #пока не переделал эту часть под задание по часовой стрелке
    def copy(self):
        return Physics_polygon(self.geom.copy())
