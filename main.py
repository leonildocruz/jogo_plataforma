import pygame
import sys

from settings import *
from player import Player
from level import Level
from menu import Menu

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

player = Player()

level = Level()

menu = Menu()

game_state = "menu"

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    game_state = "game"

    if game_state == "game":

        player.update(level.platforms)

        screen.fill(BLUE)

        level.draw(screen)

        player.draw(screen)

    else:

        menu.draw(screen)

    pygame.display.flip()

pygame.quit()

sys.exit()