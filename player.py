import pygame
from settings import *

class Player:

    def __init__(self):

        self.rect = pygame.Rect(100, 500, 40, 60)

        self.vel_y = 0

        self.on_ground = False


    def update(self, platforms):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = JUMP_FORCE
            self.on_ground = False

        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        self.on_ground = False

        for platform in platforms:

            if self.rect.colliderect(platform):

                if self.vel_y > 0:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True


    def draw(self, screen):

        pygame.draw.rect(screen, RED, self.rect)