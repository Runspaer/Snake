import time
class Map:
    def __init__(self,objs):
        self.objs=objs
    def tick(self):
        for i in range(len(self.objs)):
            self.objs[i].tick()
    def collision(self):
        clash_obj = []
        for i in range(len(self.objs)):
            for j in range(i+1,len(self.objs)):
                cl=self.objs[i].is_collision(self.objs[j])#столкнувшиеся объекты и нормаль для первого объекта и для второго
                if cl:
                    print(cl[2])
                    print()
                    # time.sleep(5)
                    cl[0].react_on_clash(cl[1],cl[2][1])
                    cl[1].react_on_clash(cl[0],cl[2][0])
                    clash_obj.append(cl[0])
                    clash_obj.append(cl[1])
        return clash_obj
                #if self.objs[i].phys.is_collision(self.objs[j].phys):
    #                 # for i in self.objs[i].phys.geom.give_gl_peaks():
    #                 #     print(i.x,i.y)
    #                 # for i in self.objs[j].phys.geom.give_gl_peaks():
    #                 #     print(i.x, i.y)
    #
    #                 #time.sleep(5)
    #
    #                 self.objs[i].eat(screen_size)
    #                 self.objs[j].eat(screen_size)
