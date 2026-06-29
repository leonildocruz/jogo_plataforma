import pygame
from settings import *

class Level:

    def __init__(self):

        self.platforms = [

            # Chão
            pygame.Rect(0, HEIGHT - 80, WIDTH, 80),

            # Plataformas
            pygame.Rect(220, 560, 180, 20),
            pygame.Rect(470, 470, 180, 20),
            pygame.Rect(760, 390, 180, 20),
            pygame.Rect(1030, 300, 180, 20),

        ]

    def draw(self, screen):

        # Chão
        pygame.draw.rect(screen, (100, 70, 30), self.platforms[0])

        # Plataformas
        for platform in self.platforms[1:]:
            pygame.draw.rect(screen, (120, 90, 40), platform)