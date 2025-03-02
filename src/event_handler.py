import pygame
def handle_events(birds):
    """
    Processa eventos do jogo, como teclas pressionadas.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            for bird in birds:
                bird.jump()
