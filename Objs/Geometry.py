import pygame
from Objs.Plane.Point import *

class Geometry:
    def __init__(self,center:Point,peaks,color):
        self.center=center
        self.peaks=peaks
        self.color=color
    def give_gl_peaks(self):
        return [i+self.center for i in self.peaks]
    def draw(self,screen):
        pass
    def copy(self):
        return Geometry(self.center,self.peaks,self.color)

class Geometry_circle(Geometry):
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.center.x, self.center.y), self.peaks[0].abs())
    def copy(self):
        return Geometry_circle(self.center,self.peaks,self.color)


class Geometry_polygon(Geometry):
    def draw(self, screen):
        coord=self.give_gl_peaks()
        coord=[[i.x,i.y] for i in coord]
        pygame.draw.polygon(screen, self.color, coord)
    def copy(self):
        return Geometry_polygon(self.center,self.peaks,self.color)
