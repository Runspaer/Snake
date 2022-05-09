import pygame
from Controllers.Objs.Plane.Point import *

class Geometry:
    def __init__(self,peaks,color):
        self.peaks=peaks
        self.color=color
    def give_gl_peaks(self,center):
        return [i+center for i in self.peaks]
    def draw(self,screen,center):
        pass
    def copy(self):
        return Geometry(self.peaks,self.color)

class Geometry_circle(Geometry):
    def draw(self,screen,center):
        pygame.draw.circle(screen, self.color, (center.x, center.y), self.peaks[0].abs())
    def copy(self):
        return Geometry_circle(self.peaks,self.color)


class Geometry_polygon(Geometry):
    def draw(self, screen,center):
        coord=self.give_gl_peaks(center)
        coord=[[i.x,i.y] for i in coord]
        pygame.draw.polygon(screen, self.color, coord)
    def copy(self):
        return Geometry_polygon(self.peaks,self.color)