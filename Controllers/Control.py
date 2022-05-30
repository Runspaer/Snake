import csv

from Controllers.Objs.Obj import *
from random import randrange

class Control:
    def __init__(self,objs,regular_csv=None,circle_csv=None):
        if type(objs)==list:
            self.objs=objs
        else:
            self.objs = [objs]
        if regular_csv!=None:
            self.read_csv(regular_csv)

    def tick(self):
        for i in self.objs:
            i.tick()
    def draw(self,screen):
        for i in self.objs:
            i.draw(screen)
    def read_csv(self,name_regular_csv):
        pass

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

    def read_csv(self,regular_csv):
        with open(regular_csv, 'r') as f:
            include_obj = csv.reader(f, delimiter=';')
            next(include_obj)
            for i in include_obj:
                center = Point(float(i[0]), float(i[1]))

                pointers = i[2].split(',')
                peaks = []
                for j in range(0,len(pointers),2):
                    peaks.append(Point(float(pointers[j]), float(pointers[j + 1])))

                color, triangle_geom, velocity, triangle_vel = i[3], float(i[4]), Point(float(i[5]), float(i[6])), float(i[7])

                self.objs.append(Apple(Physics_polygon(center,peaks,color,triangle_geom,velocity,triangle_vel)))


class Walls_Control(Control):
    def read_csv(self, regular_csv):
        with open(regular_csv, 'r') as f:
            include_obj = csv.reader(f, delimiter=';')
            next(include_obj)
            for i in include_obj:
                center = Point(float(i[0]), float(i[1]))

                pointers = i[2].split(',')
                peaks = []
                for j in range(0, len(pointers), 2):
                    peaks.append(Point(float(pointers[j]), float(pointers[j + 1])))

                color, triangle_geom, velocity, triangle_vel = i[3], float(i[4]), Point(float(i[5]),float(i[6])), float(i[7])
                self.objs.append(Wall(Physics_polygon(center, peaks, color, triangle_geom, velocity, triangle_vel)))


class Snake_Control1(Control):
    def __init__(self,objs,buttons):#objs, но там только одна змея
        super().__init__(objs)
        self.buttons=buttons
    def tick(self):
        for i in self.objs:
            i.tick(self.buttons)
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
