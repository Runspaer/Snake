import pygame.transform

from Controllers.Objs.Obj import *
import numpy as np
import math as m
class Snake(Obj):
    def __init__(self,phys:Physics):
        super().__init__(phys)
        self.tail=[]#Physics

    def tick(self,buttons):
        # #мем
        # for i in self.phys.geom.peaks:
        #     i.x, i.y = np.dot(np.array([[m.cos(m.radians(2)), -m.sin(m.radians(2))], [m.sin(m.radians(2)), m.cos(m.radians(2))]],float), np.array([i.x, i.y], float))

        for i in range(1,len(self.tail)):
            self.tail[-i]=self.tail[-i-1].copy()
            # self.tail[-i].coord+=self.tail[-i].vel
            # self.tail[-i].vel=self.tail[-i-1].vel
        if self.tail:
            self.tail[0] = self.copy()#??? как быть, если делать всё physics

        self.phys.tick(buttons)

    def draw(self,screen):
        for i in self.tail:
            i.phys.draw(screen)
        self.phys.draw(screen)

    def eat(self, screen_size):#Добавлено для единообразия
        if not self.tail:
            cop=self.phys.copy()
            cop.geom.center-=self.phys.vel
            self.tail.append(Obj(cop))##Интересная проблема с указателями в питоне, нужно будет рассказать
        cop=self.tail[-1].phys.copy()
        cop.geom.center-=self.tail[-1].phys.vel
        self.tail.append(Obj(cop))
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