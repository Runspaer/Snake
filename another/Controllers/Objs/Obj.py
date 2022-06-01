from another.Controllers.Objs.Physics import *

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
        clash_perp=self.phys.is_collision(other.phys)
        if clash_perp:
            return clash_perp
        return False

class Tail(Obj):
    def copy(self):
        return Tail(self.phys.copy())

class Wall(Obj):
    def __init__(self,phys:Physics):
        super().__init__(phys)
    def react_on_clash(self,other,clash_norm):
        pass
    def tick(self,buttons):
        self.phys.tick(buttons)


class Apple(Obj):
    def copy(self):
        return Apple(self.phys.copy())

    def react_on_clash(self,other,clash_norm):#Умирает
        self.is_visibl=False

    def give_max_distance(self):
        peaks=self.phys.geom.peaks
        max_x=abs(peaks[0].x)
        max_y=abs(peaks[0].y)

        for i in peaks:
            if abs(i.x)>max_x: max_x=abs(i.x)
            if abs(i.y)>max_y: max_y=abs(i.y)
        return [max_x,max_y]
