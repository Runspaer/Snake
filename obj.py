from vector import *
import pygame
class Obj:
    def __init__(self,glob_coord:Point,loc_vel:Point,color):
        self.glv = glob_coord
        self.locv = loc_vel
        self.color=color
    def tick(self):
        pass
    def draw(self,screen):
        pass

class Circle(Obj):
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.vec.glv[0],self.vec.glv[1]), (self.vec.size[0]**2+self.vec.size[1]**2)**0.5)

class Wall(Obj):
    def draw(self,screen):
        pygame.draw.line(screen,self.color,(self.vec.glv[0],self.vec.glv[1]),(self.vec.glv[0]+self.vec.size[0],self.vec.glv[1]+self.vec.size[1]),10)
class Rect_void(Obj):
    def __init__(self,vec:Vector,color,vertical:Vector):
        super().__init__(vec, color)
        self.vertical=vertical
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, ((self.vec.glv-self.vec.size-self.vertical.size),(self.vec.glv+self.vec.size+self.vertical.size)), 5)
        #pygame.draw.line(screen, self.color, (self.vec.glv-self.vec.size-self.vertical.size),(self.vec.glv+self.vec.size+self.vertical.size), 10)
        #pygame.draw.rect(screen,self.color,((self.vec.glv[0]-self.vec.size[0],self.vec.glv[1]-self.vec.size[1]),(self.vec.glv[0]+self.vec.size[0],self.vec.glv[1]+self.vec.size[1])))
        #pygame.draw.line(screen,self.color,(self.vec.glv[0],self.vec.glv[1]),(self.vec.glv[0]+self.vec.size[0],self.vec.glv[1]+self.vec.size[1]),10)
    #def collision(self,head):
    #    for i in range(len(self.vec)):
    #        M1 = np.array([[self.vec[i].vec[0], self.vec[i].vec[1]]])  # Матрица (левая часть системы)
