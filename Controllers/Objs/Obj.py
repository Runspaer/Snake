from random import randrange
from Controllers.Objs.Physics import *

class Obj:
    def __init__(self,phys:Physics):
        self.phys = phys
        self.is_visibl=True
    def tick(self):
        self.phys.tick()
    def draw(self,screen):
        self.phys.draw(screen)
    def react_on_clash(self,other,clash_norm):
        pass
    def copy(self):
        return Obj(self.phys.copy())
    def is_collision(self,other):
        pass
    #     if self.phys.is_collision(other):
    #         return True
    #     return False

class Wall(Obj):
    def __init__(self,phys:Physics):
        super().__init__(phys)
        #self.sight=sight#Обозначает сдвиг изображения
    def react_on_clash(self,other,clash_norm):
        pass

class Dead_wall(Wall):
    def react_on_clash(self,other,clash_norm):#Убивает сущетво, которе прикоснулось к ней
        pass


class Apple(Obj):
    def react_on_clash(self,other,clash_norm):#Умирает
        self.is_visibl=False
    def is_collision(self,other):
        return other.is_collision(self)
    #def collision(self,head,screen_size):
    #    for i in range(len(self.vec)):
    #        if (((self.vec[i].beg[0]-head.beg[0])**2+(self.vec[i].beg[1]-head.beg[1])**2)**0.5)<=(self.vec[i].size()+head.size()):
    #            self.vec.pop(i)
    #            beg=[randrange(0, screen_size[0], 20), randrange(0, screen_size[1], 20)]
    #            self.vec.append(Vector(beg, [beg[0]+10,beg[1]]))
    #            return 0
    #        return 1