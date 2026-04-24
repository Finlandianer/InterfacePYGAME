import pygame
from pathlib import Path

BASE = Path(__file__).parent

def load_bg():
    céu      = pygame.image.load(BASE / "bg1.png").convert_alpha()
    nuvem1  = pygame.image.load(BASE / "bg3.png").convert_alpha()
    nuvem2= pygame.image.load(BASE / "bg4.png").convert_alpha()
    vento       = pygame.image.load(BASE / "bg6.png").convert_alpha()
    nuvemsecundaria = pygame.image.load(BASE / "bg5.png").convert_alpha()
    nuvemprincipal = pygame.image.load(BASE / "bg2.png").convert_alpha()
    moinho = pygame.image.load(BASE / "moinho.png").convert_alpha()
    return [céu, nuvem1, nuvem2, vento, nuvemsecundaria, nuvemprincipal, moinho]

def draw_bg(screen, load_bg, scroll, Screen_width, Screen_height):

    bg_images = load_bg

    bg_width = bg_images[0].get_width()
    bg_height = bg_images[0].get_height()
    tiles_x = (Screen_width // bg_width) + 2
    tiles_y = (Screen_height // bg_height) + 2 # Calcula o número de tiles necessários para cobrir a tela
    velocidades = [0.1, 0.5, 0.45, 0.4, 0.5, 0.6, 0] # Velocidades de rolagem para cada layer

    for layer_index, img in enumerate(bg_images): # Para cada layer de fundo
        speed = velocidades[layer_index] # Velocidade de rolagem para cada layer
        offset = int(scroll * speed) % bg_width # Calcula o deslocamento horizontal para o layer atual
        for x in range(tiles_x):
            for y in range(tiles_y):
                screen.blit(img, (x * bg_width - offset, y * bg_height)) # Efeito parallax