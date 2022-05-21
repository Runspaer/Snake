from Visual.UI import *
from Engine import *
#from Visual.Include_me import include_objs
from Visual.include_me import *


class Controller:
    def __init__(self):
        objs,screen_size = include_objs()
        self.ui = UI(screen_size)

        self.engine = Engine(screen_size, Map(objs))

        self.start_game()

    def start_game(self):
        runGame = True
        while runGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: runGame = False
            else:
                self.engine.tick()
                self.ui.draw(self.engine.map.objs)
