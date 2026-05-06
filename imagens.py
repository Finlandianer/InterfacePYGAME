import pygame

def load_images():

    # ---------- LOAD ----------
    background = pygame.image.load("assets/1.png").convert_alpha()
    sol = pygame.image.load("assets/3.png").convert_alpha()
    montanhas = pygame.image.load("assets/2.png").convert_alpha()
    #nuvens = pygame.image.load("assets/nuvens.png").convert_alpha()

    moinho = pygame.image.load("assets/moinho.png").convert_alpha() #sheet

    return background, sol, montanhas, moinho