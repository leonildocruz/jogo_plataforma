# portal.py
import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            self.image = pygame.image.load("assets/images/items/portal.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 60))
        except:
            self.image = pygame.Surface((50, 60))
            self.image.fill((255, 0, 255)) # Quadrado rosa de fallback
            
        self.rect = self.image.get_rect(topleft=(x, y))