import pygame
import os


class Assets:

    def __init__(self):

        self.background = pygame.image.load(
            os.path.join("assets", "images", "background", "background.png")
        ).convert()

        self.player = pygame.image.load(
            os.path.join("assets", "images", "player", "player.png")
        ).convert_alpha()

        self.enemy = pygame.image.load(
            os.path.join("assets", "images", "enemies", "enemy.png")
        ).convert_alpha()

        self.coin = pygame.image.load(
            os.path.join("assets", "images", "items", "coin.png")
        ).convert_alpha()

        self.portal = pygame.image.load(
            os.path.join("assets", "images", "items", "portal.png")
        ).convert_alpha()