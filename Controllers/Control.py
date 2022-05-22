from Controllers.Objs.Obj import *
from random import randrange
import pandas as pd

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
    def read_csv(self,name_csv):
        include_obj=pd.read_csv(name_csv,sep=';')
        for i in include_obj.head():
            print(include_obj[i][0])
        # self.objs=Apples_Control([Apple(Physics_circle(Point(50,50),10,3,'red',0,Point(0,0),0)),Apple(Physics_circle(Point(50,50),10,16,'red',0,Point(0,0),0))])


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
        apple.phys.center=Point(randrange(int(max_x)+5, screen_size[0]-(int(max_x)+5), 20),randrange(int(max_y)+5, screen_size[1]-(int(max_y)+5), 20))
        return apple


class Walls_Control(Control):
    pass

class Snake_Control1(Control):
    def __init__(self,objs,buttons):#objs, но там только одна змея
        super().__init__(objs)
        self.buttons=buttons
    def tick(self):
        self.objs[0].tick(self.buttons)
    def is_collision(self, other):
        for i in self.objs:
            for j in other.objs:
                clash_perp=i.is_collision(j)
                if clash_perp:
                    return [i,j,clash_perp[0],clash_perp[1]]
        return False

class Buttons:
    def __init__(self,left,right):
        self.left=left
        self.right=right

