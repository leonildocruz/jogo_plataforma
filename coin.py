# coin.py
import pygame
from settings import *

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        try:
            # Caminho relativo apontando para a sua imagem de moeda
            self.image = pygame.image.load("assets/images/items/coin.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (30, 30))
        except:
            # Caso não encontre a imagem, cria o quadrado amarelo usando o TILE_SIZE que causou o erro
            self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE // 2))
            self.image.fill((255, 215, 0)) # Amarelo ouro
            
        self.rect = self.image.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))