from UI import *
from Engine import *
class Controller:
    def __init__(self):
        screen_size=[500,500]
        self.ui=UI(screen_size)
        self.engine=Engine(screen_size,Map([Snake(Point(screen_size[0]//2,screen_size[1]//2),Point(1,1),'green',10,[]),Apple(Point(10,10),Point(0,0),'red',5)]))

        self.start_game()
    def start_game(self):
        runGame=True
        while runGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: runGame = False
            else:
                self.engine.tick()
                self.ui.draw(self.engine.map.objs)