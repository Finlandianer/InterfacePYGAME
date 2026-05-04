import pygame
import imagens

all_sprites = pygame.sprite.LayeredUpdates()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale, layer):
        super().__init__()

        w = image.get_width()
        h = image.get_height()

        self.image = pygame.transform.scale(
            image,
            (int(w * scale), int(h * scale))
        )

        self.rect = self.image.get_rect(topleft=(x, y))

        self.clicked = False
        self.action = False
        self._layer = layer

    def update(self):
        self.action = False

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.action = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

class Moinho(pygame.sprite.Sprite):

    def __init__(self, x, y, spritesheet, frame_width, frame_height, num_frames, layer):
        super().__init__()

        # ---------- LAYER ----------
        self._layer = layer

        # ---------- CORTAR SPRITESHEET ----------
        self.frames = []

        for i in range(num_frames):
            frame = spritesheet.subsurface(
                (i * frame_width, 0, frame_width, frame_height)
            )
            self.frames.append(frame)

        # ---------- ANIMAÇÃO ----------
        self.frame_index = 0
        self.animation_speed = 0.15

        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))

    # ---------- UPDATE ----------
    def update(self):

        # avançar animação
        self.frame_index += self.animation_speed

        # reiniciar quando acabar
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        # trocar imagem
        self.image = self.frames[int(self.frame_index)]