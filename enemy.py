import pygame


class Enemy:

    def __init__(self, image, x, y):

        self.image = pygame.transform.scale(image, (50, 50))

        self.rect = pygame.Rect(x, y, 40, 50)

        self.direction = 1

        self.speed = 2

        self.min_x = x - 120

        self.max_x = x + 120


    def update(self):

        self.rect.x += self.speed * self.direction

        if self.rect.x <= self.min_x:
            self.direction = 1

        if self.rect.x >= self.max_x:
            self.direction = -1


    def draw(self, screen):

        screen.blit(self.image, (self.rect.x - 5, self.rect.y))