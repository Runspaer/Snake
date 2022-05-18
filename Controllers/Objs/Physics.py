from Controllers.Objs.Geometry import *
from Controllers.Objs.Plane.Simplex import *
import math as m
import numpy as np
from pygame import key
#Тесты
import time

class Enum:
    def __init__(self,left,right):
        self.left=left
        self.right=right
#ОООООчень неправильно, но может сработать
class Side:
    def __init__(self, global_peaks,center):#содержит гольбальные координаты векторов, образующих сторону и центр
        self.global_peaks=global_peaks
        self.center=center
    def find_furthest_point(self, direction: Point):
        pointers = self.global_peaks
        max_point = Point(0, 0)
        max_r = -10000000000000000000
        for i in pointers:
            if i * direction > max_r:
                max_r = i * direction
                max_point = i
        return max_point
    def perp_outside(self,colliding_obj_vel):
        a = self.global_peaks[0]
        b = self.global_peaks[1]
        ab = b - a
        abPerp = ab.perp()
        ao= self.center - a

        # Проверяем направление перпендикуляра, он должен
        # быть направлен против фигуры
        if abPerp * ao >= 0:
            abPerp = -abPerp

        if abPerp*colliding_obj_vel<0:
            return abPerp
        return False



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

    def find_furthest_point(self, direction:Point):
        pass

    def is_collision(self,other):
        if self.GJK(other):
            collision_pointers=self.GJK(other)
            # Из-за проблемы с коллизией будем выкручиваться, проверяем, что оба объекта не являются кругами,
            # если нашли хотя бы один не круг, то всё хорошо и делаем отражение относительное его стороны, иначе просто делаем отскок на 90 градусов

            if len(self.geom.peaks)!=1 and len(other.geom.peaks)!=1:
                # Выбираем объект с которым будем сталкивать, он не должен быть кругом
                if len(self.geom.peaks)!=1:
                    colliding_obj = self
                    clash_obj=other
                    collision_peaks = collision_pointers[1]
                else:
                    colliding_obj = other
                    clash_obj=self
                    collision_peaks = collision_pointers[0]
                print(colliding_obj)

                #Теперь мы проходим составляем из точек стороны фигуры, чтобы понять, с какой именно стороной произошло пересечение.
                #У нас будет три варианта для сторон

                for i in range(3):#Так как у нас всегда функция возвращает 3 точки
                    # Создаём сторону и проверяем, что найденная сторона действительно является частью фигуры

                    colisiion_Side=Side([collision_peaks[i],collision_peaks[(i+1)%3]],clash_obj.center)#%3 так как длина 3
                    side=collision_peaks[i]-collision_peaks[(i+1)%3]

                    flag=False
                    for j in clash_obj.geom.give_side():
                        if (side.x==j.x and side.y==j.y) or (-side.x==j.x and -side.y==j.y):
                            flag=True
                            break
                    if flag:
                        #Проверяем пересечение
                        if colliding_obj.GJK(colisiion_Side):
                            collision_perp = colisiion_Side.perp_outside(colliding_obj.vel)
                            if collision_perp:

                                if self==colliding_obj:
                                    return [collision_perp,-collision_perp]
                                return [-collision_perp,collision_perp]

            return [-self.vel,-other.vel]
        return False

    def clash(self,other):
        pass

    def support(self, B, direction: Point):
        return self.find_furthest_point(direction) - B.find_furthest_point(-direction)#-r

    def GJK(self,B):
        direction=Point(1,0)# можно выбрать любое начальное направление, давайте возьмём 1 0
        support = self.support(B,direction)
        # запоминаем, какие координаты первой фигуры учитывались в симплексе
        collision_pointers_first=[self.find_furthest_point(direction)]

        # запоминаем, какие координаты второй фигуры учитывались в симплексе
        collision_pointers_second=[B.find_furthest_point(-direction)]

        simplex=Simplex([support],collision_pointers_first,collision_pointers_second)

        #Смотрим по обратному направлению, так как мы ищем ближайшую точку к началу координат.
        #Если наша изначальная точка совпала с ближайшей точкой к началу координат, то пересечения точно нет
        direction = -support
        while direction:
            support = self.support(B, direction)
            #Если новая точка не находится в направлении поиска, то тогда мы выходим и пересечения нет
            #Т.е. функция поддержки вернула точку, которая уже была самой дальней в направлении
            if support * direction <= 0:
                return False
            simplex.push_back(support,self.find_furthest_point(direction),B.find_furthest_point(-direction))
            direction = simplex.CalculateDirection()
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
        # print(collision_pointers_second[0].x, collision_pointers_second[0].y, 'aaaaaa')
        # time.sleep(5)
        return [simplex.collision_pointers_first,simplex.collision_pointers_second]

    def rebound(self,clash_norm):
        # print(clash_norm.x,clash_norm.y)
        clash_norm=Point(clash_norm.x/clash_norm.abs(), clash_norm.y/clash_norm.abs())
        print(clash_norm.x, clash_norm.y,' norm')
        #
        # self.vel+=i
        # self.center -= Point(self.vel.x * 10, self.vel.y * 10)
        # #Тесты
        # print(i.x, i.y)
        # print(self.vel.x, self.vel.y)
        if abs(((clash_norm * self.vel) / (self.vel.abs())))>1:
            a = m.degrees(m.acos(-1))
        else:
            a = m.degrees(
                m.acos((clash_norm * self.vel) / (self.vel.abs()))) - 90  # угол в градусах
        # if a<0:
        #     print(a,clash_norm.x,clash_norm.y)
        #     time.sleep(20)
        # #Тесты
        print(2*(self.vel.abs()**2),' vel value')
        print(1-m.cos(m.radians(2*a)),' triangle')
        d=m.sqrt(2*(self.vel.abs()**2)*(1-m.cos(m.radians(2*a))))
        print(d,'d')
        clash_norm=Point(clash_norm.x*d,clash_norm.y*d)
        print(clash_norm.x, clash_norm.y,' new_norm')
        print(self.vel.x,self.vel.y,' vel_old')
        #time.sleep(2)
        self.vel=self.vel+clash_norm
        print(self.vel.x, self.vel.y, ' vel_new')
        print()
    def tick_no_turn(self):
        self.center+=self.vel




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