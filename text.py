import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da janela
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Button Example')

# Definir as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Definir a fonte
font = pygame.font.SysFont(None, 55)

# Função para desenhar um botão
def draw_button(screen, color, rect, text):
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    screen.blit(text_surface, text_rect)

# Função para verificar se o botão foi clicado
def is_button_clicked(rect, pos):
    return rect[0] <= pos[0] <= rect[0] + rect[2] and rect[1] <= pos[1] <= rect[1] + rect[3]

# Loop principal do jogo
running = True
while running:
    screen.fill(WHITE)

    # Definir o botão
    button_rect = pygame.Rect(300, 250, 200, 100)
    draw_button(screen, BLUE, button_rect, 'Click Me')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_button_clicked(button_rect, event.pos):
                print("Button clicked!")

    pygame.display.flip()

pygame.quit()
sys.exit()
