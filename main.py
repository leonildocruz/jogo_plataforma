# main.py
import pygame
import sys
from settings import *
from menu import draw_menu
from level import Level

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

def draw_text_screen(screen, text, subtext, color):
    screen.fill(BLACK)
    font_large = pygame.font.SysFont(None, 64)
    font_small = pygame.font.SysFont(None, 36)
    
    surf_text = font_large.render(text, True, color)
    surf_sub = font_small.render(subtext, True, WHITE)
    
    screen.blit(surf_text, (WIDTH//2 - surf_text.get_width()//2, HEIGHT//2 - 50))
    screen.blit(surf_sub, (WIDTH//2 - surf_sub.get_width()//2, HEIGHT//2 + 50))

def main():
    game_state = "MENU" 
    level = Level()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if game_state == "MENU":
                    if event.key == pygame.K_RETURN:
                        game_state = "PLAYING"
                elif game_state in ["GAME_OVER", "WIN"]:
                    if event.key == pygame.K_RETURN:
                        level = Level() # Reinicia a fase
                        game_state = "PLAYING"

        if game_state == "MENU":
            draw_menu(screen)
            
        elif game_state == "PLAYING":
            screen.fill(BLUE)
            level_status = level.run(screen)
            
            if level_status == "GAME_OVER":
                game_state = "GAME_OVER"
            elif level_status == "WIN":
                game_state = "WIN"
            
        elif game_state == "GAME_OVER":
            draw_text_screen(screen, "VOCÊ MORREU!", "Pressione ENTER para tentar novamente", (255, 0, 0))
            
        elif game_state == "WIN":
            draw_text_screen(screen, "VOCÊ VENCEU!", "Parabéns! Pressione ENTER para jogar de novo", (0, 255, 0))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()