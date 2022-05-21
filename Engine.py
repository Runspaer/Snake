from Map import *
#Плохая идея, но пока сделаю так
from Controllers.Control import Apples_Control

from random import randrange
class Engine:
    def __init__(self,screen_size : list,map: Map):
        self.screen_size = screen_size
        self.map=map
    def tick(self):
        self.map.tick()
        clash_obj=self.map.collision()
        for i in clash_obj:
            if not i.is_visibl:
                for j in self.map.objs:
                    if type(j)==Apples_Control:
                        if j.find_and_spawn(i,self.screen_size):
                            break