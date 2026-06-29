import pygame
import sys

from settings import *
from player import Player
from enemy import Enemy
from level import Level
from menu import Menu
from assets_loader import Assets

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

assets = Assets()

player = Player(assets.player)

enemy = Enemy(assets.enemy, 600, HEIGHT - 130)

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

        enemy.update()

        screen.blit(
            pygame.transform.scale(
                assets.background,
                (WIDTH, HEIGHT)
            ),
            (0, 0)
        )

        level.draw(screen)

        enemy.draw(screen)

        player.draw(screen)

    else:

        menu.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()