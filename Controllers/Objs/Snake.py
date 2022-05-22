import pygame.transform

from Controllers.Objs.Obj import *
import numpy as np
import math as m
from random import randint
class Snake(Obj):
    def __init__(self,phys:Physics,score_point:Point,skin=None):#Возможно будет ошибкой добавлять сюда координаты счётчика, но пусть пока будет так
        if skin!=None:
            phys.geom.color=skin[0]
        super().__init__(phys)
        self.tail=[]#Tail
        self.score_point=score_point
        self.skin=skin

    def tick(self,buttons):
        # #мем
        # for i in self.phys.geom.peaks:
        #     i.x, i.y = np.dot(np.array([[m.cos(m.radians(2)), -m.sin(m.radians(2))], [m.sin(m.radians(2)), m.cos(m.radians(2))]],float), np.array([i.x, i.y], float))

        for i in range(1,len(self.tail)):
            self.tail[-i].tick()#Использует стандартный tick из Obj
            self.tail[-i].phys.vel=self.tail[-i-1].phys.vel.copy()#Помни про указатели
        if self.tail:
            self.tail[0].tick()  # Использует стандартный tick из Obj
            self.phys.tick(buttons)
            self.tail[0].phys.vel = self.phys.vel.copy()# Помни про указатели
        else:
            self.phys.tick(buttons)
        # # Тесты
        # print(self.phys.vel.x, self.phys.vel.y)
        # time.sleep(0.01)


    def draw(self,screen):
        self.phys.draw(screen)
        for i in self.tail:
            i.phys.draw(screen)
        #Можно даже сделать как класс, но это уже будет усложнение, пока оставлю так
        font_score = pygame.font.SysFont('Arial', 20, bold=True)
        render_score = font_score.render(f'Score: {len(self.tail)//2}',1,self.phys.geom.color)
        screen.blit(render_score,(self.score_point.x,self.score_point.y))

    def is_collision(self,other):
        clash_perp=self.phys.is_collision(other.phys)
        if clash_perp:
            return clash_perp
        return False

    def eat(self):
        #Сразу содаём 2 цвета, которые мы поместим в наши новые хвосты
        color=[]
        # По стандарту просто рандом
        if self.skin==None:
            for i in range(2):
                color.append((randint(1,255),randint(1,255),randint(1,255)))
        else:
            color.append(self.skin[(len(self.tail)+1)%len(self.skin)])#+1, так как первый цвет будет у головы
            color.append(self.skin[(len(self.tail)+1) % len(self.skin)])

        if not self.tail:
            cop=self.phys.copy()
            cop.triangle_vel=0
            cop.center-=self.phys.vel
            cop.geom.color=color[0]
            self.tail.append(Tail(cop))##Интересная проблема с указателями в питоне, нужно будет рассказать

        else:
            # Яблоки поворота
            # for i in self.tail:
            #     i.phys.triangle_geom+=1

            cop = self.tail[-1].phys.copy()
            cop.triangle_vel = 0
            cop.center -= self.tail[-1].phys.vel
            cop.geom.color = color[0]
            self.tail.append(Tail(cop))

        cop=self.tail[-1].phys.copy()
        cop.matpov_vel = np.array([[1, 0], [0, 1]], float)
        cop.center-=self.tail[-1].phys.vel
        cop.geom.color = color[1]
        self.tail.append(Tail(cop))
        #Прикол
        # for i in range(10):
        #     cop = self.tail[-1].phys.copy()
        #     cop.matpov_vel = np.array([[1, 0], [0, 1]], float)
        #     cop.center -= self.tail[-1].phys.vel
        #     self.tail.append(Tail(cop))

    def rebound(self,clash_norm):
        self.phys.rebound(clash_norm)
        self.tick_no_turn()
        for i in range(1, len(self.tail)):
            self.tail[-i].tick_no_turn()  # Использует стандартный tick из Obj
            self.tail[-i].phys.vel = self.tail[-i - 1].phys.vel.copy()  # Помни про указатели
        if self.tail:
            self.tail[0].tick_no_turn()  # Использует стандартный tick из Obj
            self.tail[0].phys.vel = self.phys.vel.copy()  # Помни про указатели

    def react_on_clash(self,other,clash_norm):
        if type(other)==Apple:
            # Яблоки поворота
            #self.phys.triangle_geom += 1

            self.eat()
        if type(other)==Wall:
            self.rebound(clash_norm)


            #pygame.draw.circle(screen, i.color, (i.coord.x, i.coord.y), i.r)
    # def clash(self,other):
    #     pass
    #     norm=other.give_clash_norm()# лист, который содержит нормаль к центру и против цента
    #     for i in norm:
    #         if i*self.vel<=0:#выбираем нормаль к центру
    #             print(i.x, i.y)
    #             print(self.vel.x, self.vel.y)
    #             a=m.degrees(m.acos(i*self.vel/(self.vel.ro(Point(0,0))*i.ro(Point(0,0)))))-90#угол в градусах
    #             print(a)
    #             a=2*a
    #             print(a)
    #             v1=Point(0,0)
    #             v1.x, v1.y = np.dot(np.array(
    #                     [[m.cos(m.radians(a)), -m.sin(m.radians(a))], [m.sin(m.radians(a)), m.cos(m.radians(a))]],
    #                     float), np.array([self.vel.x, self.vel.y], float))
    #             if i*v1>=0:
    #                 self.vel.x,self.vel.y=v1.x,v1.y
    #             else:
    #                 self.vel.x, self.vel.y = np.dot(np.array(
    #                         [[m.cos(m.radians(a)), m.sin(m.radians(a))], [-m.sin(m.radians(a)), m.cos(m.radians(a))]],
    #                         float), np.array([self.vel.x, self.vel.y], float))
    #             print(self.vel.x,self.vel.y)
    #             print()
    #             break
    #             #Надо будет переделать поворот и сделать вместо этого просто сложение векторов, задавать объекты по кругу, чтобы сразу была правильная нормаль и всё было норм