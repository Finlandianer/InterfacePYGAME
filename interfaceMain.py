import pygame
import Btn_Sys
import imagens


def main():
    pygame.init()

    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 512

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Interface Main")
    clock = pygame.time.Clock()
    FPS = 60

    # Carregar imagens
    bg_img, novo_img, cont_img = imagens.load_images()

    # Criar objetos
    background = Btn_Sys.Background(bg_img)
    novo_jogo = Btn_Sys.Button(300, 250, novo_img, 0.6, 1)
    continuar = Btn_Sys.Button(300, 350, cont_img, 0.6, 1)

    # Adicionar sprites ao grupo
    Btn_Sys.all_sprites.add(background, layer=0)
    Btn_Sys.all_sprites.add(novo_jogo, layer=1)
    Btn_Sys.all_sprites.add(continuar, layer=1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if novo_jogo.is_clicked(event.pos):
                    print("Novo Jogo clicado!")
                elif continuar.is_clicked(event.pos):
                    print("Continuar clicado!")

        # Atualizar e desenhar
        Btn_Sys.all_sprites.update()
        Btn_Sys.all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()