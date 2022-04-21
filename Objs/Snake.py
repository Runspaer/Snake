import pygame.transform

from Objs.Obj import *
import numpy as np
import math as m
class Snake(Circle):
    def __init__(self,coord:Point,vel:Point,color,r:int,tail:list):
        super().__init__(coord,vel,color,r)
        self.tail=tail#Circle
        self.head=pygame.image.load('Visual/Head.png')
        self.head = pygame.transform.scale(self.head, (self.r * 2,self.r * 2))  # Только столкновение по диагонали выглядит криво, так как объект состоит из пикселей и не является идеальным кругом
        self.body = pygame.image.load('Visual/Body.png')
        self.body = pygame.transform.scale(self.body, (self.r * 2,
                                                       self.r * 2))  # Только столкновение по диагонали выглядит криво, так как объект состоит из пикселей и не является идеальным кругом
    def tick(self):
        for i in range(1,len(self.tail)):
            self.tail[-i]=self.tail[-i-1].copy()
            # self.tail[-i].coord+=self.tail[-i].vel
            # self.tail[-i].vel=self.tail[-i-1].vel
        if self.tail:
            self.tail[0] = Circle(self.coord, self.vel, 'green', self.r)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.vel.x,self.vel.y=np.dot(np.array([[m.cos(m.radians(5)),-m.sin(m.radians(5))],[m.sin(m.radians(5)),m.cos(m.radians(5))]],float),np.array([self.vel.x,self.vel.y],float))
        if keys[pygame.K_LEFT]:
            self.vel.x,self.vel.y = np.dot(np.array([[m.cos(m.radians(5)),m.sin(m.radians(5))], [-m.sin(m.radians(5)), m.cos(m.radians(5))]],float),np.array([self.vel.x,self.vel.y],float))
        self.coord+=self.vel
    def draw(self,screen):
        for i in self.tail:
            screen.blit(self.body, self.body.get_rect(center=(i.coord.x,i.coord.y)))
        if self.vel.y<=0:# так как у нас ось Y располагается сверху вниз
            head = pygame.transform.rotate(self.head,m.degrees(m.acos(self.vel.x/self.vel.ro(Point(0,0)))))
        else:
            head = pygame.transform.rotate(self.head, m.degrees(-m.acos(self.vel.x / self.vel.ro(Point(0, 0)))))
        #self.head=pygame.transform.rotate(self.head,m.acos(self.vel*Point(1,0)/(self.coord.ro(Point(0,0)))))
        circle = head.get_rect(center=(self.coord.x,self.coord.y))
        screen.blit(head,circle)

    def eat(self, screen_size):#Добавлено для единообразия
        if not self.tail:
            self.tail.append(Circle(self.coord - self.vel, self.vel, 'green', self.r))
        else:
            self.tail.append(
                Circle(self.tail[-1].coord - self.tail[-1].vel, self.tail[-1].vel, 'green', self.tail[-1].r))
            #pygame.draw.circle(screen, i.color, (i.coord.x, i.coord.y), i.r)
    def clash(self,other):
        pass
        norm=other.give_clash_norm()# лист, который содержит нормаль к центру и против цента
        for i in norm:
            if i*self.vel<=0:#выбираем нормаль к центру
                print(i.x, i.y)
                print(self.vel.x, self.vel.y)
                a=m.degrees(m.acos(i*self.vel/(self.vel.ro(Point(0,0))*i.ro(Point(0,0)))))-90#угол в градусах
                print(a)
                a=2*a
                print(a)
                v1=Point(0,0)
                v1.x, v1.y = np.dot(np.array(
                        [[m.cos(m.radians(a)), -m.sin(m.radians(a))], [m.sin(m.radians(a)), m.cos(m.radians(a))]],
                        float), np.array([self.vel.x, self.vel.y], float))
                if i*v1>=0:
                    self.vel.x,self.vel.y=v1.x,v1.y
                else:
                    self.vel.x, self.vel.y = np.dot(np.array(
                            [[m.cos(m.radians(a)), m.sin(m.radians(a))], [-m.sin(m.radians(a)), m.cos(m.radians(a))]],
                            float), np.array([self.vel.x, self.vel.y], float))
                print(self.vel.x,self.vel.y)
                print()
                break