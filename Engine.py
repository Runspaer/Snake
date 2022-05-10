from Map import *
#Плохая идея, но пока сделаю так
from Controllers.Objs.Snake import *

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
                if type(i)==Apple:#Пусть лучше у меня будет яблоко перемещаться, так как иначе придётся кидывать ссылку на класс яблок и будет неудобно работать
                    i.phys.center=Point(randrange(i.phys.geom.peaks[0].abs()+5, self.screen_size[0]-(i.phys.geom.peaks[0].abs()+5), 20),
                                             randrange(i.phys.geom.peaks[0].abs()+5, self.screen_size[1]-(i.phys.geom.peaks[0].abs()+5), 20))
