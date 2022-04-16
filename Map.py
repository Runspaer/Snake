import time
class Map:
    def __init__(self,objs):
        self.objs=objs
    def tick(self):
        for i in range(len(self.objs)):
            self.objs[i].tick()
    def collision(self):
        for i in range(len(self.objs)):
            for j in range(i+1,len(self.objs)):
                if self.objs[i].collision(self.objs[j]):
                    time.sleep(10)