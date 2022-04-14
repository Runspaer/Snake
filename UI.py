import pygame
class UI:
    def __init__(self,screen_size):
        self.screen_size=screen_size
        pygame.init()
        # Параметры окна
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Змейка")
    def draw(self,obj: list):
        pygame.time.delay(20)
        self.screen.fill((0, 0, 0))
        for i in range(len(obj)):
            obj[i].draw(self.screen)
        pygame.display.update()