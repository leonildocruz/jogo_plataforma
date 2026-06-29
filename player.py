import pygame
from settings import *


class Player:

    def __init__(self, image):

        self.image = pygame.transform.scale(image, (50, 50))

        self.rect = pygame.Rect(100, 500, 40, 50)

        self.vel_y = 0

        self.on_ground = False


    def update(self, platforms):

        keys = pygame.key.get_pressed()

        dx = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -PLAYER_SPEED

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = PLAYER_SPEED

        self.rect.x += dx

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

        screen.blit(self.image, (self.rect.x - 5, self.rect.y))