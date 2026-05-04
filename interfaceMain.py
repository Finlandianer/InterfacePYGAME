import pygame
import btn_sys
import imagens

pygame.init()

# ================= CONFIG =================
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512

btnposx = 624
njposy = 170
cjposy = njposy + 75
exposy = njposy + 150

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Warden Arcanus")

clock = pygame.time.Clock()
FPS = 60


# ================= IMAGENS =================
layer_far, layer_mid, layer_near, layer_front, layer_bg, moinho_sheet = imagens.load_images()


# ================= OBJETOS =================

# ---- fundos parados ----
background = btn_sys.background(0, 0, layer_bg, 1, 0)
front_static = btn_sys.background(200, 0, layer_front, 1, 0)

# ---- parallax ----
# Distribuição visual melhorada do parallax
layer_far_height = layer_far.get_height()
layer_mid_height = layer_mid.get_height()
layer_near_height = layer_near.get_height()
layer_bg_height = layer_bg.get_height()

# Posicionamento centralizado para cobertura visual completa
parallax_y_far = (SCREEN_HEIGHT - layer_far_height) // 2
parallax_y_mid = (SCREEN_HEIGHT - layer_mid_height) // 2
parallax_y_near = (SCREEN_HEIGHT - layer_near_height) // 2

clouds_far = btn_sys.Parallax(layer_far, parallax_y_far, 0.15, 1)
clouds_mid = btn_sys.Parallax(layer_mid, parallax_y_mid, 0.3, 2)
clouds_near = btn_sys.Parallax(layer_near, parallax_y_near, 0.5, 3)

# ---- botões ----
novo_jogo = btn_sys.Button(btnposx, njposy, "NOVO JOGO", 6)
continuar = btn_sys.Button(btnposx, cjposy, "CONTINUAR", 6)
sair = btn_sys.Button(btnposx, exposy, "SAIR", 6)

# ---- animação moinho ----
moinho = btn_sys.Moinho(0, 10, moinho_sheet, 512, 512, 4, 5)


# ================= SPRITES NORMAIS =================
btn_sys.all_drawable.add(moinho)
btn_sys.all_drawable.add(novo_jogo)
btn_sys.all_drawable.add(continuar)
btn_sys.all_drawable.add(sair)


# ================= LOOP =================
running = True
while running:

    # ---------- EVENTOS ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------- UPDATE ----------
    btn_sys.all_drawable.update()

    clouds_far.update()
    clouds_mid.update()
    clouds_near.update()

    # ---------- AÇÕES DOS BOTÕES ----------
    if novo_jogo.action:
        print("Novo jogo")

    if continuar.action:
        print("Continuar")

    if sair.action:
        running = False

    # ---------- DRAW ----------
    screen.fill((0, 0, 0))

   # 1️⃣ background (mais fundo)
    screen.blit(background.image, background.rect)

    # 2️⃣ front_static (atrás dos objetos)
    screen.blit(front_static.image, front_static.rect)

    # 3️⃣ parallax
    clouds_far.draw(screen)
    clouds_mid.draw(screen)
    clouds_near.draw(screen)

    # 4️⃣ sprites e UI (na frente)
    btn_sys.all_drawable.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()