import pygame
from Objs.Plane.Simplex import *
import math as m
class Obj:
    def __init__(self,coord:Point,vel:Point,color):
        self.coord = coord
        self.vel = vel
        self.color=color
    def give_clash_norm(self):
        pass
    def tick(self):
        pass
    def draw(self,screen):
        pass
    def search_points(self):# находит все вершины фигуры
        pass
    def collision(self,other):
        return self.GJK(other)
    def clash(self,other):
        pass
    def find_furthest_point(self, direction:Point):
        pointers=self.search_points()
        max_point = Point(0,0)
        max_r = -10000000000000000000
        for i in pointers:
            if i * direction > max_r:
                max_r = i * direction
                max_point = i
        return max_point

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

class Circle(Obj):
    def __init__(self,coord:Point,vel:Point,color,r:int):
        super().__init__(coord,vel, color)
        self.r=r
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.coord.x,self.coord.y),self.r)
    def find_furthest_point(self, direction:Point):
        angle=m.atan2(direction.y, direction.x)
        return Point(self.coord.x + (self.r * m.cos(angle)),self.coord.y + (self.r * m.sin(angle)))
    def copy(self):
        return Circle(self.coord,self.vel,self.color,self.r)


class Size_wall(Obj):
    def __init__(self,coord:Point,vel:Point,color,w:int,h:int,sight:Point):
        super().__init__(coord,vel, color)
        self.w=w
        self.h=h
        self.sight=sight#Обозначает сдвиг изображения
    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.coord.x+self.w-self.sight.x, self.coord.y+self.h-self.sight.y),(self.coord.x-self.w-self.sight.x, self.coord.y -self.h-self.sight.y), 1)
    def search_points(self):# находит все вершины фигуры
        return [self.coord+Point(self.w,self.h),self.coord-Point(self.w,self.h)]
    def give_clash_norm(self):# в будущем можно будет находить вектор, где произошло стокновение и возвращать его
        return [(self.search_points()[0]-self.search_points()[1]).norm(),(self.search_points()[1]-self.search_points()[0]).norm()]

#class Wall(Obj):
#    def draw(self,screen):
#        pygame.draw.line(screen,self.color,(self.vec.glv[0],self.vec.glv[1]),(self.vec.glv[0]+self.vec.size[0],self.vec.glv[1]+self.vec.size[1]),10)
'''
class Rect_void(Obj):
    def __init__(self,coord:Point,vel:Point,color,w:int,h:int):
        super().__init__(coord,vel, color)
        self.w=w
        self.h=h
    def draw(self,screen):
        pass
    #    pygame.draw.rect(screen, self.color, ((self.vec.glv-self.vec.size-self.vertical.size),(self.vec.glv+self.vec.size+self.vertical.size)), 5)
        #pygame.draw.line(screen, self.color, (self.vec.glv-self.vec.size-self.vertical.size),(self.vec.glv+self.vec.size+self.vertical.size), 10)
        #pygame.draw.rect(screen,self.color,((self.vec.glv[0]-self.vec.size[0],self.vec.glv[1]-self.vec.size[1]),(self.vec.glv[0]+self.vec.size[0],self.vec.glv[1]+self.vec.size[1])))
        #pygame.draw.line(screen,self.color,(self.vec.glv[0],self.vec.glv[1]),(self.vec.glv[0]+self.vec.size[0],self.vec.glv[1]+self.vec.size[1]),10)
    #def collision(self,head):
    #    for i in range(len(self.vec)):
    #        M1 = np.array([[self.vec[i].vec[0], self.vec[i].vec[1]]])  # Матрица (левая часть системы)
'''