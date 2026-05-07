import pygame
import btn_sys
import imagens

pygame.init()

# ================= CONFIG =================
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512

btnposx = 650 #button x position
njposy = 150 #novo jogo y position
cjposy = njposy + 75 #continuar jogo y position
exposy = njposy +  150 #exit y position

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Warden Arcanus")

clock = pygame.time.Clock()
FPS = 60


# ================= IMAGENS =================
bg_surface, sol_surface, montanhas_surface, moinho_sheet = imagens.load_images()

# ---- fundos parados e detalhes ----
background = btn_sys.background(0, 0, bg_surface, 1.8, 0)

sol_static = btn_sys.background(200, 0, sol_surface, 1.0, 1)

sun_glow = btn_sys.Glow(
    sol_static, 0, (255, 220, 120),0)

vignette = btn_sys.Vignette(
    SCREEN_WIDTH,SCREEN_HEIGHT,350, sol_static, 999)

# ---- parallax A FAZER OU REMOVER ----
montanhas = btn_sys.background(0, 25, montanhas_surface, 1, 1)
#nuvens = btn_sys.background(0, 0, nuvens_surface, 1, 2) usável quando tiver a imagem

# --------------------------------botões -----------------------------------------
novo_jogo = btn_sys.Button(btnposx, njposy, "NOVO JOGO", 6)
continuar = btn_sys.Button(btnposx, cjposy, "CONTINUAR", 6)
sair = btn_sys.Button(btnposx, exposy, "SAIR", 6)

# ---- animação moinho ----
moinho = btn_sys.Moinho(0, 10, moinho_sheet, 512, 512, 4, 5)


# ================= SPRITES NORMAIS =================
btn_sys.all_drawable.add(moinho)
#btn_sys.all_drawable.add(nuvens) usável quando tiver a imagem
btn_sys.all_drawable.add(montanhas)
btn_sys.all_drawable.add(sol_static)

# ================= EVENTOS PRINCIPAIS =================
running = True
while running:

    # ---------- EVENTOS ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------- UPDATE ----------
    btn_sys.all_drawable.update()

    # ---------- AÇÕES DOS BOTÕES ----------
    if novo_jogo.action:
        print("67") #lógica após clicar no botão

    if continuar.action:
        print("Nill Kiggas") #lógica após clicar no botão

    if sair.action:
        running = False #clicou, saiu

    # ---------- DRAW ----------
    screen.fill((0, 0, 0))

   # 1. background (estático e atrás de tudo)
    screen.blit(background.image, background.rect)

    # 2. sol_static (atrás de uns, na frente de outros)
    screen.blit(sol_static.image, sol_static.rect)

    # 3. sprites e UI (na frente, uso de all_drawable para facilitar a ordem de desenho nas camadas)
    btn_sys.all_drawable.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()