import time
from Controllers.Control import Snake_Control1
class Map:
    def __init__(self,objs):
        self.objs=objs
    def tick(self):
        for i in range(len(self.objs)):
            self.objs[i].tick()
    def collision(self):
        clash_obj = []
        for i in range(len(self.objs)):
            if type(self.objs[i])==Snake_Control1:
                for j in range(len(self.objs)):
                    if self.objs[j]!=self.objs[i]:
                        cl=self.objs[i].is_collision(self.objs[j])#столкнувшиеся объекты и нормаль для первого объекта и для второго
                        if cl:
                            # time.sleep(5)
                            first_collision_obj,second_collision_obj,first_perp,second_perp=cl
                            first_collision_obj.react_on_clash(second_collision_obj,first_perp)
                            second_collision_obj.react_on_clash(first_collision_obj,second_perp)
                            clash_obj.append(first_collision_obj)
                            clash_obj.append(second_collision_obj)
        return clash_obj

