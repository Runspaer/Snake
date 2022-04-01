from Apple import *
from Snake import *
from obj import *
class Map:
    def __init__(self,obj):
        self.obj=obj
    def tick(self):
        for i in range(len(self.obj)):
            self.obj[i].tick()
    #def collision(self,screen_size):
    #    a=self.obj[1].collision(self.obj[0].vec[0],screen_size)
    #    if a==0:
    #        self.obj[0].eat()
