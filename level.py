import pygame
from settings import *

class Level:

    def __init__(self):

        self.platforms = [

            pygame.Rect(0, HEIGHT-80, WIDTH, 80),      # chão

            pygame.Rect(250, 550, 200, 30),

            pygame.Rect(550, 450, 220, 30),

            pygame.Rect(900, 350, 220, 30),

            pygame.Rect(500, 250, 180, 30),

        ]


    def draw(self, screen):

        for platform in self.platforms:
            pygame.draw.rect(screen, BROWN, platform)