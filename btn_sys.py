import pygame

all_drawable = pygame.sprite.LayeredUpdates()


# ================= BACKGROUND =================

class background(pygame.sprite.Sprite):

    def __init__(self, x, y, image, scale, layer):
        super().__init__()

        self._layer = layer
        self.image = pygame.transform.smoothscale(
            image,
            (int(image.get_width() * scale), int(image.get_height() * scale))
        )
        self.rect = self.image.get_rect(topleft=(x, y))
        
# ================= BUTTON =================
class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, text, layer):
        super().__init__()

        self._layer = layer

        self.text = text
        self.font = pygame.font.Font("assets/fontes/monogram.ttf", 55)

        self.base_color = (230, 230, 230)
        self.hover_color = (255, 255, 255)

        # animação
        self.base_scale = 1.0
        self.hover_scale = 1.04
        self.current_scale = 1.0
        self.animation_speed = 0.15

        self.clicked = False
        self.action = False

        # cria texto inicial
        self.create_surface(self.base_color)

        self.rect = self.image.get_rect(center=(x, y))

    # -------------------------
    def create_surface(self, color):

        text_surface = self.font.render(self.text, True, color)

        # fundo transparente
        self.base_surface = text_surface
        self.image = text_surface

    # -------------------------
    def update(self):

        mouse_pos = pygame.mouse.get_pos()
        hovering = self.rect.collidepoint(mouse_pos)

        # muda cor
        color = self.hover_color if hovering else self.base_color
        self.create_surface(color)

        # escala suave
        target_scale = self.hover_scale if hovering else self.base_scale
        self.current_scale += (
            target_scale - self.current_scale
        ) * self.animation_speed

        w = self.base_surface.get_width()
        h = self.base_surface.get_height()

        new_size = (int(w * self.current_scale),
                    int(h * self.current_scale))

        center = self.rect.center

        self.image = pygame.transform.smoothscale(
            self.base_surface,
            new_size
        )

        self.rect = self.image.get_rect(center=center)

        # clique
        self.action = False

        if hovering:
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.action = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

# ================= MOINHO =================
class Moinho(pygame.sprite.Sprite):


    def __init__(self, x, y, spritesheet, frame_width, frame_height, num_frames, layer):
        super().__init__()

        self._layer = layer

        self.frames = []

        for i in range(num_frames):
            frame = spritesheet.subsurface(
                (i * frame_width, 0, frame_width, frame_height)
            )
            self.frames.append(frame)

        self.frame_index = 0
        self.animation_speed = 0.17

        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):

        self.frame_index += self.animation_speed

        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]

    def draw(self, surface):

        for x in self.positions:
            surface.blit(self.image, (x, self.y))