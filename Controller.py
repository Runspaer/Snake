from Visual.UI import *
from Engine import *
from Visual.Include_me import include_objs


class Controller:
    def __init__(self):
        screen_size = [500, 500]
        self.ui = UI(screen_size)
        objs = include_objs(screen_size)
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
