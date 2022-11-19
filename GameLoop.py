import math

import pygame
radiusc = 128

class GameView:
    fillament = (255, 64, 72)
    def __init__(self, wide, tall):
        self.wide = wide
        self.tall = tall
        pygame.init()
        self.window = pygame.display.set_mode((self.wide, self.tall))
        self.x = self.wide / 2
        self.y = self.wide / 2

    # hello 🦒 ✌

    def run(self):
        running = True
        while running:

            eventList = pygame.event.get()
            for event in eventList:
                if event.type == pygame.QUIT:
                    running = False
                    break
            pygame.draw.circle(surface= self.window, color=self.fillament, center=(self.x, self.y-radiusc/math.pi), radius=radiusc)
            pygame.display.update()



        pygame.quit()

