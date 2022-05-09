from Controllers.Objs.Geometry import *
from Controllers.Objs.Plane.Simplex import *
import math as m
import numpy as np
from pygame import key

class Enum:
    def __init__(self,left,right):
        self.left=left
        self.right=right


class Physics:
    def __init__(self,center:Point,geom:Geometry,triangle_geom,velocity,triangle_vel):#считаем, что изначально всё крутиться против часовой стрелки
        self.center=center
        self.geom=geom
        self.vel=velocity
        self.matpov_geom = np.array([[m.cos(m.radians(triangle_geom)), m.sin(m.radians(triangle_geom))],
                                    [-m.sin(m.radians(triangle_geom)), m.cos(m.radians(triangle_geom))]], float)
        self.matpov_vel= np.array([[m.cos(m.radians(triangle_vel)), m.sin(m.radians(triangle_vel))],
                                   [-m.sin(m.radians(triangle_vel)), m.cos(m.radians(triangle_vel))]],float)
        #Нужны для точного копирования
        self.triangle_geom=triangle_geom
        self.triangle_vel=triangle_vel
    def draw(self,screen):
        self.geom.draw(screen,self.center)
    #Надо сделать
    def tick(self,buttons=None):
        if buttons==None:
            self.vel.x, self.vel.y = np.dot(self.matpov_vel, np.array([self.vel.x, self.vel.y], float))
            self.center += self.vel
        else:
            keys = pygame.key.get_pressed()
            if keys[buttons.left]:
                self.vel.x, self.vel.y = np.dot(self.matpov_vel, np.array([self.vel.x, self.vel.y], float))
                # for i in self.geom.peaks:
                #     i.x, i.y = np.dot(self.matpov_vel, np.array([i.x, i.y], float))
            if keys[buttons.right]:
                self.vel.x, self.vel.y = np.dot(np.linalg.inv(self.matpov_vel), np.array([self.vel.x, self.vel.y], float))# пока взял обратную, думаю, что не будет сильно бить по эффективности
                # for i in self.geom.peaks:
                #       i.x, i.y = np.dot(np.linalg.inv(self.matpov_vel), np.array([i.x, i.y], float))
            self.center += self.vel
        for i in self.geom.peaks:
            i.x, i.y = np.dot(self.matpov_geom, np.array([i.x, i.y], float))
    def copy(self):
        return Physics(self.center,self.geom.copy(),self.vel,self.triangle_geom,self.triangle_vel)
    #Переделать, так как не имеет смысла
    def give_clash_norm(self):
        pass
    def find_furthest_point(self, direction:Point):
        pass
    def is_collision(self,other):
        return self.GJK(other)
    def clash(self,other):
        pass
    def support(self, B, direction: Point):  # r A B #A B r
        return self.find_furthest_point(direction) - B.find_furthest_point(Point(-direction.x,-direction.y))#-r
    def GJK(self,B):
        support = self.support(B,Point(1,0))# r a b # a b r
        simplex=Simplex([support])
        direction = Point(-1, 0)
        while direction:
            support = self.support(B, direction)
            if support * direction <= 0:
                return False
            simplex.push_back(support)
            direction = simplex.CalculateDirection()
        return True


class Physics_circle(Physics):
    def __init__(self,center:Point,peaks,color,triangle_geom,velocity,triangle_vel):
        super().__init__(center,Geometry_circle(peaks,color),triangle_geom,velocity,triangle_vel)
    def find_furthest_point(self, direction:Point):
        angle=m.atan2(direction.y, direction.x)
        return Point(self.center.x + (self.geom.peaks[0].abs() * m.cos(angle)),self.center.y + (self.geom.peaks[0].abs() * m.sin(angle)))
    def copy(self):
        return Physics_circle(self.center,self.geom.peaks,self.geom.color,self.vel,self.triangle_geom,self.triangle_vel)

class Physics_polygon(Physics):
    def __init__(self,center:Point,peaks,color,triangle_geom,velocity,triangle_vel):
        super().__init__(center,Geometry_polygon(peaks,color),triangle_geom,velocity,triangle_vel)
    def find_furthest_point(self, direction:Point):
        pointers=self.geom.give_gl_peaks(self.center)
        max_point = Point(0,0)
        max_r = -10000000000000000000
        for i in pointers:
            if i * direction > max_r:
                max_r = i * direction
                max_point = i
        return max_point
    def give_clash_norm(self):# в будущем можно будет находить вектор, где произошло стокновение и возвращать его
        return [(self.geom.give_gl_peaks(self.center)[0]-self.geom.give_gl_peaks(self.center)[1]).norm(),
                (self.geom.give_gl_peaks(self.center)[1]-self.geom.give_gl_peaks(self.center)[0]).norm()]
        #пока не переделал эту часть под задание по часовой стрелке

    def copy(self):
         return Physics_polygon(self.center,self.geom.peaks,self.geom.color,self.vel,self.triangle_geom,self.triangle_vel)
