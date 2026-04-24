import pygame
from backgroundPlx import *

pygame.init()

Clock = pygame.time.Clock()
FPS = 60

Screen_width = 1024
Screen_height = 512

screen = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("Mi bombonada")

background = pygame.image.load("background.png")
screen.blit(background, (0, 0))

bg_images = load_bg()
scroll = 0

running = True
while running:
    Clock.tick(FPS)

    scroll += 0.4

    draw_bg(screen, bg_images, scroll, Screen_width, Screen_height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()