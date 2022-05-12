from Controllers.Objs.Geometry import *
from Controllers.Objs.Plane.Simplex import *
import math as m
import numpy as np
from pygame import key
#Для тестов
import time

class Enum:
    def __init__(self,left,right):
        self.left=left
        self.right=right
#ОООООчень неправильно, но может сработать
class Line:
    def __init__(self, global_peaks):#Только 2 элемента, так как линия
        self.global_peaks=global_peaks

    def find_furthest_point(self, direction: Point):
        pointers = self.global_peaks
        max_point = Point(0, 0)
        max_r = -10000000000000000000
        for i in pointers:
            if i * direction > max_r:
                max_r = i * direction
                max_point = i
        return max_point
    def perp(self):
        return (self.global_peaks[0]-self.global_peaks[1]).perp()


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

    def tick(self,buttons=None):
        if buttons==None:
            self.vel.x, self.vel.y = np.dot(self.matpov_vel, np.array([self.vel.x, self.vel.y], float))
            self.center += self.vel
        else:
            keys = pygame.key.get_pressed()
            if keys[buttons.left]:
                self.vel.x, self.vel.y = np.dot(self.matpov_vel, np.array([self.vel.x, self.vel.y], float))

                # Альтернативный способ поворота
                # for i in self.geom.peaks:
                #     i.x, i.y = np.dot(self.matpov_vel, np.array([i.x, i.y], float))
            if keys[buttons.right]:
                self.vel.x, self.vel.y = np.dot(np.linalg.inv(self.matpov_vel), np.array([self.vel.x, self.vel.y], float))# пока взял обратную, думаю, что не будет сильно бить по эффективности

                # Альтернативный способ поворота
                # for i in self.geom.peaks:
                #       i.x, i.y = np.dot(np.linalg.inv(self.matpov_vel), np.array([i.x, i.y], float))
            self.center += self.vel
        #Поворот
        for i in self.geom.peaks:
            i.x, i.y = np.dot(self.matpov_geom, np.array([i.x, i.y], float))

    def copy(self):
        return Physics(self.center.copy(),self.geom.copy(),self.triangle_geom,self.vel.copy(),self.triangle_vel)

    #Переделать, так как теперь должно нести новый смысл
    def find_furthest_point(self, direction:Point):
        pass

    def is_collision(self,other):
        if self.GJK(other):
            collision_pointers_first, collision_pointers_second=self.GJK(other)
            for i in range(len(collision_pointers_first)):
                colisiion_line=Line([collision_pointers_first[i],collision_pointers_first[(i+1)%len(collision_pointers_first)]])
                if other.GJK(colisiion_line):
                    collision_pointers_first=colisiion_line.perp()
                    # #Тесты
                    # for i in colisiion_line.global_peaks:
                    #     print(i.x,i.y, 'aaaaaaaaaa')
                    break
            for i in range(len(collision_pointers_second)):
                colisiion_line=Line([collision_pointers_second[i],collision_pointers_second[(i+1)%len(collision_pointers_second)]])
                if other.GJK(colisiion_line):
                    collision_pointers_second=colisiion_line.perp()
                    break
            return [collision_pointers_first,collision_pointers_second]
        return False

    def clash(self,other):
        pass

    def support(self, B, direction: Point):
        return self.find_furthest_point(direction) - B.find_furthest_point(Point(-direction.x,-direction.y))#-r

    def GJK(self,B):
        direction=Point(1,0)# можно выбрать любое начальное направление, давайте возьмём 1 0
        support = self.support(B,direction)

        #Сейчас будем считать столкновение только с одной из фигур,
        #разницы в теории нет, максимум может мешать круг, но это мы выясним позже

        #Уже переделал, так что тут считаются оба, мб сейчас переделаем

        collision_pointers_first=[self.find_furthest_point(direction)]
        collision_pointers_second=[B.find_furthest_point(Point(-direction.x,-direction.y))]
        simplex=Simplex([support],collision_pointers_first,collision_pointers_second)

        #Смотрим по обратному направлению, так как мы ищем ближайшую точку к началу координат.
        #Если наша изначальная точка совпала с ближайшей точкой к началу координат, то пересечения точно нет
        direction = Point(-support.x, -support.y)
        while direction:
            support = self.support(B, direction)
            #Если новая точка не находится в направлении поиска, то тогда мы выходим и пересечения нет
            #Т.е. функция поддержки вернула точку, которая уже была самой дальней в направлении
            if support * direction <= 0:
                return False
            simplex.push_back(support,self.find_furthest_point(direction),B.find_furthest_point(Point(-direction.x,-direction.y)))
            direction = simplex.CalculateDirection()
        #?????????????????????
        # #Тесты
        # for i in range(len(collision_pointers)):
        #     print(collision_pointers[i].x,collision_pointers[i].y)
        #     #print((collision_pointers[i]-collision_pointers[(i+1)%3]).x,(collision_pointers[i]-collision_pointers[(i+1)%3]).y)
        # print('pointers','\n')
        # for i in self.geom.give_gl_peaks(self.center):
        #     print(i.x,i.y)
        # print('peaks','\n')
        #Объекты столкнулись и мы знаем точки, которые участвовали в вычислении столкновений
        # #Тесты
        # print(collision_pointers_first[0].x,collision_pointers_first[0].y,'aaaaaa')
        # time.sleep(5)
        return [simplex.collision_pointers_first,simplex.collision_pointers_second]

    def rebound(self,clash_norm):
        norm = [clash_norm,
                Point(-clash_norm.x, -clash_norm.y)]  # лист, который содержит нормаль к центру и против цента
        for i in norm:
            if (i * self.vel) <= 0:  # выбираем нормаль к центру
                 # print(i.x, i.y)
                i=Point(i.x/i.abs(), i.y/i.abs())
                 #
                 # self.vel+=i
                 # self.center -= Point(self.vel.x * 10, self.vel.y * 10)
                print(i.x, i.y)
                print(self.vel.x, self.vel.y)
                a = m.degrees(
                    m.acos(i * self.vel / (self.vel.abs() * i.abs()))) - 90  # угол в градусах
                print(a)
                d=m.sqrt(2*self.vel.abs()**2*(1-m.cos(m.radians(2*a))))
                i=Point(i.x*d,i.y*d)
                self.vel=self.vel+i
                # v1 = Point(0, 0)
                # v1.x, v1.y = np.dot(np.array(
                #     [[m.cos(m.radians(a)), -m.sin(m.radians(a))], [m.sin(m.radians(a)), m.cos(m.radians(a))]],
                #     float), np.array([self.vel.x, self.vel.y], float))#Вращение по часовой
                # print(v1.x, v1.y)
                # if i * v1 >= 0:
                #     self.vel.x, self.vel.y = v1.x, v1.y
                # else:
                #     self.vel.x, self.vel.y = np.dot(np.array(
                #         [[m.cos(m.radians(a)), m.sin(m.radians(a))], [-m.sin(m.radians(a)), m.cos(m.radians(a))]],
                #         float), np.array([self.vel.x, self.vel.y], float))# Вращение против часовой
                # print(self.vel.x, self.vel.y)
                # print()
                break


class Physics_circle(Physics):
    def __init__(self,center:Point,peaks,color,triangle_geom,velocity,triangle_vel):
        super().__init__(center,Geometry_circle(peaks,color),triangle_geom,velocity,triangle_vel)

    def find_furthest_point(self, direction:Point):
        angle=m.atan2(direction.y, direction.x)# арктангенс y/x в радианах
        return Point(self.center.x + (self.geom.peaks[0].abs() * m.cos(angle)),self.center.y + (self.geom.peaks[0].abs() * m.sin(angle)))

    def copy(self):
        cop=[]
        for i in self.geom.peaks:
            cop.append(i.copy())
        return Physics_circle(self.center.copy(),cop,self.geom.color,self.triangle_geom,self.vel.copy(),self.triangle_vel)

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
        cop = []
        for i in self.geom.peaks:
            cop.append(i.copy())
        return Physics_polygon(self.center.copy(),cop,self.geom.color,self.triangle_geom,self.vel.copy(),self.triangle_vel)