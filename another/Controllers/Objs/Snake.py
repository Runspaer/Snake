import pygame.transform

from another.Controllers.Objs.Obj import *
import numpy as np
from random import randint
class Snake(Obj):
    def __init__(self,phys:Physics,score_point:Point,skin=None):
        if skin!=None:
            phys.geom.color=skin[0]
        super().__init__(phys)
        self.tail=[]#Tail
        self.score_point=score_point
        self.skin=skin
        self.left_points=0
        self.right_points = 0

    def tick(self):
        for i in range(1,len(self.tail)):
            self.tail[-i].tick()# Использует стандартный tick из Obj
            self.tail[-i].phys.vel=self.tail[-i-1].phys.vel.copy()
        if self.tail:
            self.tail[0].tick()  # Использует стандартный tick из Obj
            self.phys.tick()
            self.tail[0].phys.vel = self.phys.vel.copy()
        else:
            self.phys.tick()


    def draw(self,screen):
        self.phys.draw(screen)
        for i in self.tail:
            i.phys.draw(screen)
        font_score = pygame.font.SysFont('Arial', 40, bold=True)
        render_score = font_score.render(f'{self.left_points} Score {self.right_points}',1,self.phys.geom.color)
        screen.blit(render_score,(self.score_point.x,self.score_point.y))

    def eat(self):
        #Сразу содаём 2 цвета, которые мы поместим в наши новые хвосты
        color=[]
        # По стандарту просто рандом
        if self.skin==None:
            for i in range(2):
                color.append((randint(1,255),randint(1,255),randint(1,255)))
        else:
            color.append(self.skin[(len(self.tail)+1)%len(self.skin)])#+1, так как первый цвет будет у головы
            color.append(self.skin[(len(self.tail)+1) % len(self.skin)])

        if not self.tail:
            cop=self.phys.copy()
            cop.triangle_vel=0
            cop.center-=self.phys.vel
            cop.geom.color=color[0]
            self.tail.append(Tail(cop))

        else:
            # Яблоки поворота
            # for i in self.tail:
            #     i.phys.triangle_geom+=1

            cop = self.tail[-1].phys.copy()
            cop.triangle_vel = 0
            cop.center -= self.tail[-1].phys.vel
            cop.geom.color = color[0]
            self.tail.append(Tail(cop))

        cop=self.tail[-1].phys.copy()
        cop.matpov_vel = np.array([[1, 0], [0, 1]], float)
        cop.center-=self.tail[-1].phys.vel
        cop.geom.color = color[1]
        self.tail.append(Tail(cop))

    def rebound(self,clash_norm):
        self.phys.rebound(clash_norm)


    def react_on_clash(self,other,clash_norm):
        if type(other)==Apple:
            # Яблоки поворота
            #self.phys.triangle_geom += 1
            self.eat()
        if type(other)==Wall:
            self.rebound(clash_norm)