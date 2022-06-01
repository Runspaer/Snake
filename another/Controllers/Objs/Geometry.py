import math

import pygame
from another.Controllers.Objs.Plane.Point import *

class Geometry:
    def __init__(self,peaks,color):
        self.peaks=peaks
        self.color=color
    def give_gl_peaks(self,center):
        return [i+center for i in self.peaks]
    def draw(self,screen,center):
        pass
    def copy(self):
        cop=[]
        for i in self.peaks:
            cop.append(i.copy())
        return Geometry(cop,self.color)
    def give_side(self):
        return [self.peaks[(i+1)%len(self.peaks)] - self.peaks[i] for i in range(len(self.peaks))]

class Geometry_polygon(Geometry):
    def draw(self, screen,center):
        coord=self.give_gl_peaks(center)
        coord=[[i.x,i.y] for i in coord]
        pygame.draw.polygon(screen, self.color, coord)
    def copy(self):
        cop = []
        for i in self.peaks:
            cop.append(i.copy())
        return Geometry_polygon(cop,self.color)


class Geometry_regular_polygon(Geometry_polygon):
    def __init__(self,R,k_partitions,color):
        self.R=R
        self.k_partitions=k_partitions
        peaks=[]
        for i in range(k_partitions):
            peaks.append(Point(R*math.cos(math.radians((i+1)*360/k_partitions)),R*math.sin(math.radians((i+1)*360/k_partitions))))

        super().__init__(peaks,color)

    def copy(self):
        cop = []
        for i in self.peaks:
            cop.append(i.copy())
        return Geometry_regular_polygon(self.R,self.k_partitions,self.color)
