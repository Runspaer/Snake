from Map import *
class Engine:
    def __init__(self,screen_size : list,map: Map):
        self.screen_size = screen_size
        self.map=map
    def tick(self):
        self.map.tick()
        self.map.collision(self.screen_size)
