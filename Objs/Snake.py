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
    def tick(self):
        for i in range(1,len(self.tail)):
            self.tail[-i]=self.tail[-i-1].copy()
        if self.tail:
            self.tail[0] = Circle(Point(self.coord.x - self.vel.x, self.coord.y - self.vel.y),self.vel, 'green', self.r)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.vel.x,self.vel.y=np.dot(np.array([[m.cos(m.radians(5)),-m.sin(m.radians(5))],[m.sin(m.radians(5)),m.cos(m.radians(5))]],float),np.array([self.vel.x,self.vel.y],float))
        if keys[pygame.K_LEFT]:
            self.vel.x,self.vel.y = np.dot(np.array([[m.cos(m.radians(5)),m.sin(m.radians(5))], [-m.sin(m.radians(5)), m.cos(m.radians(5))]],float),np.array([self.vel.x,self.vel.y],float))

        self.coord+=self.vel
    def eat(self):
        if not self.tail:
            self.tail.append(Circle(Point(self.coord.x - self.vel.x, self.coord.y - self.vel.y), self.vel,'green', self.r))
        else:
            self.tail.append(Circle(Point(self.tail[-1].coord.x - self.tail[-1].vel.x, self.tail[-1].coord.y - self.tail[-1].vel.y), self.tail[-1].vel, 'green', self.tail[-1].r))
    def draw(self,screen):
        if self.vel.y<=0:# так как у нас ось Y располагается сверху вниз
            head = pygame.transform.rotate(self.head,m.degrees(m.acos(self.vel.x/self.vel.ro(Point(0,0)))))
        else:
            head = pygame.transform.rotate(self.head, m.degrees(-m.acos(self.vel.x / self.vel.ro(Point(0, 0)))))
        #self.head=pygame.transform.rotate(self.head,m.acos(self.vel*Point(1,0)/(self.coord.ro(Point(0,0)))))
        circle = head.get_rect(center=(self.coord.x,self.coord.y))
        screen.blit(head,circle)
        for i in self.tail:
            #screen.blit(head, self.head.get_rect(center=(i.coord.x,i.coord.y)))
            pygame.draw.circle(screen, i.color, (i.coord.x, i.coord.y), i.r)
    #def reaction(self,other):
        #if type(other)