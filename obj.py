from Point import *
import pygame
class Obj:
    def __init__(self,coord:Point,vel:Point,color):
        self.coord = coord
        self.vel = vel
        self.color=color
    def tick(self):
        pass
    def draw(self,screen):
        pass

class Circle(Obj):
    def __init__(self,coord:Point,vel:Point,color,r:int):
        super().__init__(coord,vel, color)
        self.r=r
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.coord.x,self.coord.y),self.r)

#class Wall(Obj):
#    def draw(self,screen):
#        pygame.draw.line(screen,self.color,(self.vec.glv[0],self.vec.glv[1]),(self.vec.glv[0]+self.vec.size[0],self.vec.glv[1]+self.vec.size[1]),10)
class Rect_void(Obj):
    def __init__(self,coord:Point,vel:Point,color,w:int,h:int):
        super().__init__(coord,vel, color)
        self.w=w
        self.h=h
    def draw(self,screen):
        pass
    #    pygame.draw.rect(screen, self.color, ((self.vec.glv-self.vec.size-self.vertical.size),(self.vec.glv+self.vec.size+self.vertical.size)), 5)
        #pygame.draw.line(screen, self.color, (self.vec.glv-self.vec.size-self.vertical.size),(self.vec.glv+self.vec.size+self.vertical.size), 10)
        #pygame.draw.rect(screen,self.color,((self.vec.glv[0]-self.vec.size[0],self.vec.glv[1]-self.vec.size[1]),(self.vec.glv[0]+self.vec.size[0],self.vec.glv[1]+self.vec.size[1])))
        #pygame.draw.line(screen,self.color,(self.vec.glv[0],self.vec.glv[1]),(self.vec.glv[0]+self.vec.size[0],self.vec.glv[1]+self.vec.size[1]),10)
    #def collision(self,head):
    #    for i in range(len(self.vec)):
    #        M1 = np.array([[self.vec[i].vec[0], self.vec[i].vec[1]]])  # Матрица (левая часть системы)
