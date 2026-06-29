# enemy.py
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            self.image = pygame.image.load("assets/images/enemies/enemy.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (40, 40))
        except:
            self.image = pygame.Surface((40, 40))
            self.image.fill((255, 0, 0))
            
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 4  # Velocidade acelerada para dar mais emoção e dificuldade!

    def update(self, tiles):
        self.rect.x += self.speed
        
        # Bate na parede/bloco lateral e volta
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):
                if self.speed > 0:
                    self.rect.right = tile.rect.left
                    self.speed *= -1
                elif self.speed < 0:
                    self.rect.left = tile.rect.right
                    self.speed *= -1
                    
        # Bate nas extremidades da tela e volta
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.speed *= -1