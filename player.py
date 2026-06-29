# player.py
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            self.image = pygame.image.load("assets/images/player/player.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        except:
            self.image = pygame.Surface((40, 40))
            self.image.fill((0, 255, 0))
            
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
        self.on_ground = False
        
        # Sistema de invulnerabilidade para não perder várias vidas de uma vez
        self.invulnerable = False
        self.hurt_time = 0

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.direction.y = self.jump_speed
            self.on_ground = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def cooldowns(self):
        if self.invulnerable:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= 1000: # 1 segundo de proteção
                self.invulnerable = False

    def update(self):
        self.get_input()
        self.cooldowns()