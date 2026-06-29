import pygame
from settings import *

class Menu:

    def __init__(self):

        self.title_font = pygame.font.SysFont("arial", 60, True)
        self.font = pygame.font.SysFont("arial", 28)

    def draw(self, screen):

        screen.fill((70, 170, 255))

        title = self.title_font.render("FOREST ESCAPE", True, WHITE)

        play = self.font.render(
            "Pressione ENTER para iniciar",
            True,
            WHITE
        )

        controls = self.font.render(
            "A/D ou Setas = Andar | ESPACO = Pular",
            True,
            WHITE
        )

        screen.blit(
            title,
            (WIDTH//2 - title.get_width()//2, 140)
        )

        screen.blit(
            play,
            (WIDTH//2 - play.get_width()//2, 280)
        )

        screen.blit(
            controls,
            (WIDTH//2 - controls.get_width()//2, 360)
        )