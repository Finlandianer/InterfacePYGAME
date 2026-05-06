import pygame
import btn_sys
import imagens

pygame.init()

# ================= CONFIG =================
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512

btnposx = 624 #button x position
njposy = 150 #novo jogo y position
cjposy = njposy + 75 #continuar jogo y position
exposy = njposy +  150 #exit y position

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Warden Arcanus")

clock = pygame.time.Clock()
FPS = 60


# ================= IMAGENS =================
background, sol, montanhas, nuvens, moinho_sheet = imagens.load_images()

# ---- fundos parados ----
background = btn_sys.background(0, 0, background, 1, 0)
sol_static = btn_sys.background(200, 0, sol, 1, 0)

# ---- botões ----
novo_jogo = btn_sys.Button(btnposx, njposy, "NOVO JOGO", 6)
continuar = btn_sys.Button(btnposx, cjposy, "CONTINUAR", 6)
sair = btn_sys.Button(btnposx, exposy, "SAIR", 6)

# ---- animação moinho ----
moinho = btn_sys.Moinho(0, 10, moinho_sheet, 512, 512, 4, 5)


# ================= SPRITES NORMAIS =================
btn_sys.all_drawable.add(moinho)
btn_sys.all_drawable.add(nuvens)
btn_sys.all_drawable.add(montanhas)
btn_sys.all_drawable.add(sol_static)

# ================= LOOP =================
running = True
while running:

    # ---------- EVENTOS ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------- UPDATE ----------
    btn_sys.all_drawable.update()

    nuvens.update()

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

    # 2️⃣ sol_static (atrás dos objetos)
    screen.blit(sol_static.image, sol_static.rect)

    # 3️⃣ parallax
   #nuvens.draw(screen)
    montanhas.draw(screen)
    sol.draw(screen)

    # 4️⃣ sprites e UI (na frente)
    btn_sys.all_drawable.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()