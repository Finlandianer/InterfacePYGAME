import pygame

def load_images():
    bg_img = pygame.image.load("assets/background.png").convert()
    novo_img = pygame.image.load("assets/novo-jogo.png").convert_alpha()
    cont_img = pygame.image.load("assets/continuar-1.png").convert_alpha()
    #exit_img = pygame.image.load("assets/exit.png").convert_alpha()
    moinho_sheet = pygame.image.load("assets/moinho.png").convert_alpha()
    
    return bg_img, novo_img, cont_img, moinho_sheet