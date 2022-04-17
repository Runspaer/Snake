from Obj import *
import numpy as np
import math as m
class Snake(Circle):
    def __init__(self,coord:Point,vel:Point,color,r:int,tail:list):
        super().__init__(coord,vel,color,r)
        self.tail=tail#Circle
    def tick(self):
        for i in range(1,len(self.tail)):
             #self.tail[-i].vel = self.tail[-i - 1].vel
                 #self.tail[-i].coord+=self.tail[-i].vel
            # if self.tail[-i].coord.ro(self.tail[-i-1].coord):
            #     self.tail[-i]=Circle(Point(self.tail[-i-1].coord.x - self.tail[-i-1].vel.x * self.tail[-i-1].r / 2, self.tail[-i-1].coord.y - self.tail[-i-1].vel.y * self.tail[-i-1].r / 2)
            #             , self.tail[-i-1].vel,'green', self.tail[-i-1].r) #дрифт
            self.tail[-i]=self.tail[-i-1].copy()
        if self.tail:
            self.tail[0] = Circle(Point(self.coord.x - self.vel.x, self.coord.y - self.vel.y),self.vel, 'green', self.r)
            # self.tail[0]=Circle(Point(self.coord.x-self.vel.x*self.r/2,self.coord.y-self.vel.y*self.r/2),self.vel,'green',self.r)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.vel.x,self.vel.y=np.dot(np.array([[m.cos(m.radians(5)),-m.sin(m.radians(5))],[m.sin(m.radians(5)),m.cos(m.radians(5))]],float),np.array([self.vel.x,self.vel.y],float))
        if keys[pygame.K_LEFT]:
            self.vel.x,self.vel.y = np.dot(np.array([[m.cos(m.radians(5)),m.sin(m.radians(5))], [-m.sin(m.radians(5)), m.cos(m.radians(5))]],float),np.array([self.vel.x,self.vel.y],float))

        self.coord+=self.vel
    def eat(self):
        if not self.tail:
            # self.tail.append(Circle(Point(self.coord.x-self.vel.x*self.r/2,self.coord.y-self.vel.y*self.r/2),self.vel,'green',self.r))
            self.tail.append(Circle(Point(self.coord.x - self.vel.x, self.coord.y - self.vel.y), self.vel,'green', self.r))
        else:
            self.tail.append(Circle(Point(self.tail[-1].coord.x - self.tail[-1].vel.x, self.tail[-1].coord.y - self.tail[-1].vel.y), self.tail[-1].vel, 'green', self.tail[-1].r))
            # self.tail.append(Circle(Point(self.tail[-1].coord.x - self.tail[-1].vel.x * self.tail[-1].r / 2, self.tail[-1].coord.y - self.tail[-1].vel.y * self.tail[-1].r / 2)
            #         , self.tail[-1].vel,'green', self.tail[-1].r)) #дрифт
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.coord.x,self.coord.y),self.r)
        for i in self.tail:
            pygame.draw.circle(screen, i.color, (i.coord.x, i.coord.y), i.r)
    #def reaction(self,other):
        #if type(other)