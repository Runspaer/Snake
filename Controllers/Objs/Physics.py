from Controllers.Objs.Geometry import *
from Controllers.Objs.Plane.Simplex import *
import numpy as np

class Side:
    def __init__(self, global_peaks,center):# содержит глобальные координаты векторов, образующих сторону, и центр
        self.global_peaks=global_peaks
        self.center=center
    def find_furthest_point(self, direction: Point):
        pointers = self.global_peaks
        max_point = Point(0, 0)
        max_r = -10000000000000000000 # Инициализировать первым из массива
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

        #Нужны для точного копирования
        self.triangle_geom=triangle_geom
        self.triangle_vel=triangle_vel

    def draw(self,screen):
        self.geom.draw(screen,self.center)

    def tick(self,buttons=None):
        matpov_geom = np.array([[np.cos(np.radians(self.triangle_geom)), np.sin(np.radians(self.triangle_geom))],
                                     [-np.sin(np.radians(self.triangle_geom)), np.cos(np.radians(self.triangle_geom))]], float)
        matpov_vel = np.array([[np.cos(np.radians(self.triangle_vel)), np.sin(np.radians(self.triangle_vel))],
                                    [-np.sin(np.radians(self.triangle_vel)), np.cos(np.radians(self.triangle_vel))]], float)
        if buttons==None:
            self.vel.x, self.vel.y = np.dot(matpov_vel, np.array([self.vel.x, self.vel.y], float))
            self.center += self.vel
        else:
            keys = pygame.key.get_pressed()
            if keys[buttons.left]:
                self.vel.x, self.vel.y = np.dot(matpov_vel, np.array([self.vel.x, self.vel.y], float))

                # Альтернативный способ поворота
                # for i in self.geom.peaks:
                #     i.x, i.y = np.dot(self.matpov_vel, np.array([i.x, i.y], float))
            if keys[buttons.right]:
                self.vel.x, self.vel.y = np.dot(np.linalg.inv(matpov_vel), np.array([self.vel.x, self.vel.y], float))# пока взял обратную, думаю, что не будет сильно бить по эффективности

                # Альтернативный способ поворота
                # for i in self.geom.peaks:
                #       i.x, i.y = np.dot(np.linalg.inv(self.matpov_vel), np.array([i.x, i.y], float))

            self.center += self.vel
        #Поворот
        for i in self.geom.peaks:
            i.x, i.y = np.dot(matpov_geom, np.array([i.x, i.y], float))

    def tick_no_turn(self):
        self.center+=self.vel

    def copy(self):
        return Physics(self.center.copy(),self.geom.copy(),self.triangle_geom,self.vel.copy(),self.triangle_vel)

    def find_furthest_point(self, direction: Point):
        pointers = self.geom.give_gl_peaks(self.center)
        max_point = Point(0, 0)
        max_r = -10000000000000000000
        for i in pointers:
            if i * direction > max_r:
                max_r = i * direction
                max_point = i
        return max_point

    def is_collision(self,other):
        if self.GJK(other):
            collision_pointers=self.GJK(other)
            col=[]

            colliding_obj = self
            clash_obj=other
            collision_peaks = collision_pointers[1]

            #Теперь мы проходим составляем из точек стороны фигуры, чтобы понять, с какой именно стороной произошло пересечение.
            #У нас будет три варианта для сторон

            for i in range(3):#Так как у нас всегда функция возвращает 3 точки
                    # Создаём сторону и проверяем, что найденная сторона действительно является частью фигуры

                colisiion_Side=Side([collision_peaks[i],collision_peaks[(i+1)%3]],clash_obj.center)#%3 так как длина 3
                side=collision_peaks[i]-collision_peaks[(i+1)%3]

                flag=False
                # print(side.x,side.y)
                for j in clash_obj.geom.give_side():
                    # print(j.x,j.y,'fig')
                    #Добавлено, так как порой последние символы считаются неправильно
                    if (round(side.x,10)==round(j.x,10) and round(side.y,10)==round(j.y,10)) or (round(-side.x,10)==round(j.x,10) and round(-side.y,10)==round(j.y,10)):
                        flag=True
                        break

                if flag:
                    #Проверяем пересечение
                    if colliding_obj.GJK(colisiion_Side):
                        # print('yes')
                        collision_perp = colisiion_Side.perp_outside(colliding_obj.vel)
                        if collision_perp:
                            col.append(collision_perp)

            min=100000000000000
            perp=[]
            if len(col)==2:
                for i in col:
                    if colliding_obj.center.ro(i)<min:
                        min=colliding_obj.center.ro(i)
                        perp=[i,-i]
                return perp
            else:
                if len(col)==1:
                    return [col[0],-col[0]]
                else:
                    # Возможно наши объекты просто зацепились, а возможно симплекс посчитан неверно,
                    # значит начинаем считать честно
                    return self.full_collision(other)
        return False

    def full_collision(self,other):
        col = []

        colliding_obj = self
        clash_obj = other

        global_points_sides=clash_obj.geom.give_gl_peaks(clash_obj.center)
        for i in range(len(global_points_sides)):
            colisiion_Side = Side([global_points_sides[i], global_points_sides[(i + 1) % len(global_points_sides)]],clash_obj.center)

            # Проверяем пересечение
            if colliding_obj.GJK(colisiion_Side):
                collision_perp = colisiion_Side.perp_outside(colliding_obj.vel)
                if collision_perp:
                    col.append(collision_perp)

        min = 100000000000000
        perp = []
        if len(col) >= 2:
            for i in col:
                if colliding_obj.center.ro(i) < min:
                    min = colliding_obj.center.ro(i)
                    perp = [i, -i]
            return perp
        else:
            if len(col) == 1:
                return [col[0], -col[0]]
            else:
                # Может получиться так, что объект догонит змею, т.е. змея отразилась, но так как объект крутиться
                # , то в следующем кадре он догонит змею и тогда происходит непонятное поведение, так что сделаем данный костыль
                if clash_obj.vel.x == 0 and clash_obj.vel.y == 0:
                    clash_obj.triangle_geom = -clash_obj.triangle_geom
                else:
                    clash_obj.vel = -clash_obj.vel
                    clash_obj.triangle_vel = -clash_obj.triangle_vel
                return False






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

        return [simplex.collision_pointers_first,simplex.collision_pointers_second]

    def rebound(self,clash_norm):

        clash_norm=Point(clash_norm.x/clash_norm.abs(), clash_norm.y/clash_norm.abs())

        if abs(((clash_norm * self.vel) / (self.vel.abs())))>1:
            a = np.degrees(np.arccos(-1))
        else:
            a = np.degrees(
                np.arccos((clash_norm * self.vel) / (self.vel.abs()))) - 90  # угол в градусах

        d=np.sqrt(2*(self.vel.abs()**2)*(1-np.cos(np.radians(2*a))))
        clash_norm=clash_norm*d
        self.vel=self.vel+clash_norm




class Physics_regular_polygon(Physics):
    def __init__(self,center:Point,R,k_partitions,color,triangle_geom,velocity,triangle_vel):
        super().__init__(center,Geometry_regular_polygon(R,k_partitions,color),triangle_geom,velocity,triangle_vel)

    def copy(self):
        return Physics_regular_polygon(self.center.copy(),self.geom.R,self.geom.k_partitions, self.geom.color,self.triangle_geom,self.vel.copy(),self.triangle_vel)

class Physics_polygon(Physics):
    def __init__(self,center:Point,peaks,color,triangle_geom,velocity,triangle_vel):
        super().__init__(center,Geometry_polygon(peaks,color),triangle_geom,velocity,triangle_vel)

    def copy(self):
        cop = []
        for i in self.geom.peaks:
            cop.append(i.copy())
        return Physics_polygon(self.center.copy(),cop,self.geom.color,self.triangle_geom,self.vel.copy(),self.triangle_vel)