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

class Apples_Control(Control):
    pass

class Walls_Control(Control):
    pass

class Snake_Control1(Control):
    def __init__(self,objs,buttons):#objs, но там только одна змея
        super().__init__(objs)
        self.buttons=buttons
    def tick(self):
        self.objs[0].tick(self.buttons)