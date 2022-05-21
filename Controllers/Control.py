from Controllers.Objs.Plane.Point import *
from random import randrange

class Control:
    def __init__(self,objs):
        if type(objs)==list:
            self.objs=objs
        else:
            self.objs = [objs]
    def tick(self):
        for i in self.objs:
            i.tick()
    def draw(self,screen):
        for i in self.objs:
            i.draw(screen)
    def is_collision(self, other):
        for i in self.objs:
            for j in other.objs:
                clash_perp=i.is_collision(j)
                if clash_perp:
                    return [i,j,clash_perp[0],clash_perp[1]]
        return False

class Apples_Control(Control):
    def find_and_spawn(self,apple,screen_size):
        for i in range(len(self.objs)):
            if self.objs[i]==apple:
                self.objs.append(self.spawn(apple,screen_size))
                self.objs.pop(i)
                return True
        return False
    def spawn(self,apple,screen_size):
        max_x,max_y=apple.give_max_distance()
        apple.phys.center=Point(randrange(max_x+5, screen_size[0]-(max_x+5), 20),randrange(max_y+5, screen_size[1]-(max_x+5), 20))
        return apple

class Walls_Control(Control):
    pass

class Snake_Control1(Control):
    def __init__(self,objs,buttons):#objs, но там только одна змея
        super().__init__(objs)
        self.buttons=buttons
    def tick(self):
        self.objs[0].tick(self.buttons)

class Enum:
    def __init__(self,left,right):
        self.left=left
        self.right=right