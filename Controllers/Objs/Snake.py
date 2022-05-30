import pygame.transform

from Controllers.Objs.Obj import *
import numpy as np
from random import randint
class Snake(Obj):
    def __init__(self,phys:Physics,score_point:Point,skin=None):#Возможно будет ошибкой добавлять сюда координаты счётчика, но пусть пока будет так
        if skin!=None:
            phys.geom.color=skin[0]
        super().__init__(phys)
        self.tail=[]#Tail
        self.score_point=score_point
        self.skin=skin

    def tick(self,buttons):
        for i in range(1,len(self.tail)):
            self.tail[-i].tick()#Использует стандартный tick из Obj
            self.tail[-i].phys.vel=self.tail[-i-1].phys.vel.copy()#Помни про указатели
        if self.tail:
            self.tail[0].tick()  # Использует стандартный tick из Obj
            self.phys.tick(buttons)
            self.tail[0].phys.vel = self.phys.vel.copy()# Помни про указатели
        else:
            self.phys.tick(buttons)


    def draw(self,screen):
        self.phys.draw(screen)
        for i in self.tail:
            i.phys.draw(screen)
        font_score = pygame.font.SysFont('Arial', 20, bold=True)
        render_score = font_score.render(f'Score: {len(self.tail)//2}',1,self.phys.geom.color)
        screen.blit(render_score,(self.score_point.x,self.score_point.y))

    def is_collision(self,other):
        clash_perp=self.phys.is_collision(other.phys)
        if clash_perp:
            return clash_perp
        return False

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
            self.tail.append(Tail(cop))##Интересная проблема с указателями в питоне, нужно будет рассказать

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
        #Прикол
        # for i in range(10):
        #     cop = self.tail[-1].phys.copy()
        #     cop.matpov_vel = np.array([[1, 0], [0, 1]], float)
        #     cop.center -= self.tail[-1].phys.vel
        #     self.tail.append(Tail(cop))

    def rebound(self,clash_norm):
        self.phys.rebound(clash_norm)

        # self.tick_no_turn()
        # for i in range(1, len(self.tail)):
        #     self.tail[-i].tick_no_turn()  # Использует стандартный tick из Obj
        #     self.tail[-i].phys.vel = self.tail[-i - 1].phys.vel.copy()  # Помни про указатели
        # if self.tail:
        #     self.tail[0].tick_no_turn()  # Использует стандартный tick из Obj
        #     self.tail[0].phys.vel = self.phys.vel.copy()  # Помни про указатели

    def react_on_clash(self,other,clash_norm):
        if type(other)==Apple:
            # Яблоки поворота
            #self.phys.triangle_geom += 1

            self.eat()
        if type(other)==Wall:
            self.rebound(clash_norm)