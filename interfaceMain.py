import pygame
import btn_sys
import imagens

pygame.init()

# ---------------- CONFIG ----------------
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512

btnposx = 390
njposy = 150
cjposy = njposy + 100
exposy = njposy + 200

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interface Main")

clock = pygame.time.Clock()
FPS = 60


# ---------------- IMAGENS ----------------
bg_img, novo_img, cont_img, moinho_sheet = imagens.load_images()


# ---------------- OBJETOS ----------------
background = btn_sys.Button(0, 0, bg_img, 1, 0)

novo_jogo = btn_sys.Button(btnposx, njposy, novo_img, 0.6, 2)
continuar = btn_sys.Button(btnposx, cjposy, cont_img, 0.6, 2)
sair = btn_sys.Button(btnposx, exposy, cont_img, 0.6, 2)

moinho = btn_sys.Moinho(
    0, 10,
    moinho_sheet,
    512, 512,
    4,
    1
)

# ---------------- LAYERS ----------------
btn_sys.all_sprites.add(background)
btn_sys.all_sprites.add(moinho)
btn_sys.all_sprites.add(novo_jogo)
btn_sys.all_sprites.add(continuar)
btn_sys.all_sprites.add(sair)


# ================= LOOP =================
running = True
while running:

    # ---------- EVENTOS ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------- UPDATE ----------
    btn_sys.all_sprites.update()

    if novo_jogo.action:
        print("Novo jogo") #apaga o print e adiciona a lógica para iniciar um novo jogo

    if continuar.action:
        print("Continuar") #apaga o print e adiciona a lógica para continuar o jogo salvo

    if sair.action:
        running = False #botao de sair fecha o jogo


    # ---------- DRAW ----------
    screen.fill((0, 0, 0))  # evita rastros visuais

    btn_sys.all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()