# level.py
import pygame
from settings import *
from player import Player
from enemy import Enemy
from portal import Portal
from coin import Coin

# Layout com exatamente 5 diamantes ('C') e 3 vilões ('E')
LEVEL_MAP = [
    '                ',
    '                ',
    ' C   E   C    W ',
    'XXXXXXXXXX   XXX',
    '                ',
    '         E  C   ',
    '    XXXXXXXXX   ',
    '  XXX           ',
    '  C           C ',
    '  P      E      ',
    'XXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXXXXXX'
]

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((139, 69, 19))
        pygame.draw.rect(self.image, (34, 139, 34), pygame.Rect(0, 0, 50, 10))
        self.rect = self.image.get_rect(topleft=(x, y))

class Level:
    def __init__(self):
        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.portal = pygame.sprite.GroupSingle()
        self.player = pygame.sprite.GroupSingle()
        
        self.score = 0
        self.lives = 3
        
        self.setup_level()
        self.status = "PLAYING"

    def setup_level(self):
        for row_index, row in enumerate(LEVEL_MAP):
            for col_index, cell in enumerate(row):
                x = col_index * 50
                y = row_index * 50
                
                if cell == 'X':
                    tile = Tile(x, y)
                    self.tiles.add(tile)
                elif cell == 'P':
                    player_sprite = Player(x, y)
                    self.player.add(player_sprite)
                elif cell == 'E':
                    enemy_sprite = Enemy(x, y)
                    self.enemies.add(enemy_sprite)
                elif cell == 'C':
                    coin_sprite = Coin(x, y)
                    self.coins.add(coin_sprite)
                elif cell == 'W':
                    portal_sprite = Portal(x, y)
                    self.portal.add(portal_sprite)

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                elif player.direction.x < 0:
                    player.rect.left = sprite.rect.right

    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False

    def check_game_states(self):
        player = self.player.sprite
        
        # AJUSTADO: Cada diamante agora soma exatamente 1 ponto, casando com a interface!
        coin_collisions = pygame.sprite.spritecollide(player, self.coins, True)
        if coin_collisions:
            self.score += len(coin_collisions) * 1
        
        # Colisão com os Inimigos (Perde 1 vida e entra em invulnerabilidade)
        if pygame.sprite.spritecollide(player, self.enemies, False):
            if not player.invulnerable:
                self.lives -= 1
                player.invulnerable = True
                player.hurt_time = pygame.time.get_ticks()
                player.rect.x -= 40
                player.direction.y = -10
                if self.lives <= 0:
                    self.status = "GAME_OVER"
                
        # Condição de Derrota por queda
        if player.rect.y > HEIGHT:
            self.status = "GAME_OVER"
            
        # Condição de Vitória: Tocar na porta após pegar todos os 5 diamantes
        if pygame.sprite.spritecollide(player, self.portal, False):
            if len(self.coins) == 0:
                self.status = "WIN"

    def draw_hud(self, screen):
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Diamantes: {self.score}", True, (255, 255, 255))
        lives_text = font.render(f"Vidas: {self.lives}", True, (255, 255, 255))
        
        # Contagem de restantes coerente de 5 a 0
        if len(self.coins) > 0:
            remaining_text = font.render(f"Restam: {len(self.coins)}", True, (255, 255, 0))
        else:
            remaining_text = font.render("Porta liberada! Entre na porta para vencer!", True, (0, 255, 0))
        
        screen.blit(score_text, (20, 20))
        screen.blit(remaining_text, (20, 50))
        screen.blit(lives_text, (WIDTH - 120, 20))

    def run(self, screen):
        self.tiles.draw(screen)
        self.coins.draw(screen)
        self.portal.draw(screen)
        self.enemies.draw(screen)
        
        player = self.player.sprite
        if not player.invulnerable or (pygame.time.get_ticks() // 100) % 2 == 0:
            self.player.draw(screen)
        
        if self.status == "PLAYING":
            self.player.update()
            self.horizontal_collision()
            self.vertical_collision()
            
            self.enemies.update(self.tiles)
            self.check_game_states()
            
        self.draw_hud(screen)
        return self.status