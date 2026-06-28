import pygame
from settings import *

class Menu:

    def __init__(self):

        self.font_title = pygame.font.SysFont("arial",60,True)

        self.font = pygame.font.SysFont("arial",30)

    def draw(self,screen):

        screen.fill((40,120,180))

        title = self.font_title.render("FOREST ESCAPE",True,WHITE)

        play = self.font.render("Pressione ENTER para Jogar",True,WHITE)

        controls = self.font.render("A/D ou Setas = Andar | ESPACO = Pular",True,WHITE)

        screen.blit(title,(WIDTH//2-title.get_width()//2,120))

        screen.blit(play,(WIDTH//2-play.get_width()//2,300))

        screen.blit(controls,(WIDTH//2-controls.get_width()//2,420))