from UI import *
from Engine import *
class Controller:
    def __init__(self):
        screen_size=[500,500]
        self.ui=UI(screen_size)
        self.engine=Engine(screen_size,Map([Snake(Vector([250,250],[1,0],[20,0])),Apple(Vector([100,100],[0,0],[0,10])),
        Rect_void(Vector([screen_size[0]//2,screen_size[1]//2],[0,0],[screen_size[0]//2,0]),(0,0,255),Vector([screen_size[0]//2,screen_size[1]//2],[0,0],[0,screen_size[1]//2]))]))

        self.start_game()
    def start_game(self):
        runGame=True
        while runGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: runGame = False
            else:
                self.engine.tick()
                self.ui.draw(self.engine.map.obj)