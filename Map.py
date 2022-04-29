from Objs.Snake import *
from Objs.Obj import Apple
import time
class Map:
    def __init__(self,objs):
        self.objs=objs
    def tick(self):
        for i in range(len(self.objs)):
            self.objs[i].tick()
    def collision(self,screen_size):
        for i in range(len(self.objs)):
            for j in range(i+1,len(self.objs)):
                # if self.objs[i].collision(self.objs[j]):
                #     if (type(self.objs[i])==Snake or type(self.objs[j])==Snake) and(type(self.objs[i])==Apple or type(self.objs[j])==Apple):
                #         self.objs[i].eat(screen_size)
                #         self.objs[j].eat(screen_size)
                #     else:
                #         self.objs[i].clash(self.objs[j])
                #         self.objs[j].clash(self.objs[i])
                if self.objs[i].phys.is_collision(self.objs[j].phys):
                    for i in self.objs[i].phys.geom.give_gl_peaks():
                        print(i.x,i.y)
                    for i in self.objs[j].phys.geom.give_gl_peaks():
                        print(i.x, i.y)

                    time.sleep(5)

                    #self.objs[i].eat(screen_size)
                    #self.objs[j].eat(screen_size)
