from Obj import Circle
from Point import Point
from random import randrange


class Apple(Circle):
    def eat(self,screen_size):
        self.coord=Point(randrange(5, screen_size[0]-5, 20), randrange(5, screen_size[1]-5, 20))
    #def collision(self,head,screen_size):
    #    for i in range(len(self.vec)):
    #        if (((self.vec[i].beg[0]-head.beg[0])**2+(self.vec[i].beg[1]-head.beg[1])**2)**0.5)<=(self.vec[i].size()+head.size()):
    #            self.vec.pop(i)
    #            beg=[randrange(0, screen_size[0], 20), randrange(0, screen_size[1], 20)]
    #            self.vec.append(Vector(beg, [beg[0]+10,beg[1]]))
    #            return 0
    #        return 1