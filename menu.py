# menu.py

import pygame
from settings import *

def draw_menu(screen):
    screen.fill(BLACK) # Preenche o fundo de preto
    
    # Configuração das fontes
    font_title = pygame.font.SysFont(None, 64)
    font_text = pygame.font.SysFont(None, 36)
    
    # Renderiza os textos
    title_surface = font_title.render("JOGO DE PLATAFORMA", True, WHITE)
    
    # Texto obrigatório com os controles
    controls_surface = font_text.render("Comandos: Setas - Mover | Espaço - Pular", True, WHITE)
    
    start_surface = font_text.render("Pressione ENTER para começar", True, YELLOW)
    
    # Posiciona os textos no centro da tela
    screen.blit(title_surface, (WIDTH//2 - title_surface.get_width()//2, 150))
    screen.blit(controls_surface, (WIDTH//2 - controls_surface.get_width()//2, 300))
    screen.blit(start_surface, (WIDTH//2 - start_surface.get_width()//2, 450))