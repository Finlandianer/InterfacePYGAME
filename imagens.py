import pygame

def load_images():

    SCREEN_W = 1024
    SCREEN_H = 512

    # ---------- LOAD ----------
    layer_far = pygame.image.load("assets/5.png").convert_alpha()
    layer_mid = pygame.image.load("assets/4.png").convert_alpha()
    layer_near = pygame.image.load("assets/3.png").convert_alpha()
    layer_front = pygame.image.load("assets/2.png").convert_alpha()
    layer_bg = pygame.image.load("assets/1.png").convert_alpha()

    moinho = pygame.image.load("assets/moinho.png").convert_alpha()

    # ---------- SCALE PROPORCIONAL ----------
    original_h = layer_bg.get_height()

    scale = SCREEN_H / original_h

    def scale_layer(img):
        w = int(img.get_width() * scale)
        h = int(img.get_height() * scale)
        return pygame.transform.scale(img, (w, h))

    layer_far = scale_layer(layer_far)
    layer_mid = scale_layer(layer_mid)
    layer_near = scale_layer(layer_near)
    layer_front = scale_layer(layer_front)
    layer_bg = scale_layer(layer_bg)

    # ---------- SCALE LARGURA PARALLAX ----------
    # Garante que as imagens parallax cubram a largura total da tela
    def ensure_width(img, min_width):
        if img.get_width() < min_width:
            scale_factor = min_width / img.get_width()
            w = int(img.get_width() * scale_factor)
            h = int(img.get_height() * scale_factor)
            return pygame.transform.scale(img, (w, h))
        return img

    layer_far = ensure_width(layer_far, SCREEN_W)
    layer_mid = ensure_width(layer_mid, SCREEN_W)
    layer_near = ensure_width(layer_near, SCREEN_W)

    return layer_far, layer_mid, layer_near, layer_front, layer_bg, moinho