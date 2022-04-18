from Objs.Snake import *
from Objs.Apple import *
class Map:
    def __init__(self,objs):
        self.objs=objs
    def tick(self):
        for i in range(len(self.objs)):
            self.objs[i].tick()
    def collision(self,screen_size):
        for i in range(len(self.objs)):
            for j in range(i+1,len(self.objs)):
                if self.objs[i].collision(self.objs[j]):
                    if type(self.objs[i])==Snake and type(self.objs[j])==Apple:
                        self.objs[i].eat()
                        self.objs[j].eat(screen_size)