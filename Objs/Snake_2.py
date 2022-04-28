import pygame.transform

from Objs.obj2 import *
import numpy as np
import math as m
class Snake(Obj):
    def __init__(self,phys:Physics,vel:Point):
        super().__init__(phys,vel)
        self.tail=[]#Physics

    def tick(self):
        for i in range(1,len(self.tail)):
            self.tail[-i]=self.tail[-i-1].copy()
            # self.tail[-i].coord+=self.tail[-i].vel
            # self.tail[-i].vel=self.tail[-i-1].vel
        if self.tail:
            self.tail[0] = self.copy()#??? как быть, если делать всё physics

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.vel.x,self.vel.y=np.dot(np.array([[m.cos(m.radians(5)),-m.sin(m.radians(5))],[m.sin(m.radians(5)),m.cos(m.radians(5))]],float),np.array([self.vel.x,self.vel.y],float))
        if keys[pygame.K_LEFT]:
            self.vel.x,self.vel.y = np.dot(np.array([[m.cos(m.radians(5)),m.sin(m.radians(5))], [-m.sin(m.radians(5)), m.cos(m.radians(5))]],float),np.array([self.vel.x,self.vel.y],float))
        self.phys.geom.center+=self.vel
    def draw(self,screen):
        for i in self.tail:
            print(i.phys.geom.center.x,i.phys.geom.center.y)
            i.phys.draw(screen)
        #print()
        self.phys.draw(screen)
    def eat(self, screen_size):#Добавлено для единообразия
        if not self.tail:
            c=self.phys.copy()
            print(c.geom.center.x, c.geom.center.y)
            c.geom.center-=self.vel
            self.tail.append(Obj(c, self.vel))##Интересная проблема с указателями в питоне, нужно будет рассказать
        else:
            c=self.tail[-1].phys.copy()
            c.geom.center-=self.tail[-1].vel
            self.tail.append(
                Obj(c, self.tail[-1].vel))
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