import pygame
import sys

from settings import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

player = Player()

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    player.update()

    screen.fill(BLUE)

    pygame.draw.rect(screen, BROWN, (0, HEIGHT-80, WIDTH, 80))

    player.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()