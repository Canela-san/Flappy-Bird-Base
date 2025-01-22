import pygame
import os

import pygame.display
import config
import bird as libbird
import pipe as libpipe
import base as libbase



# Diretório base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Sobe um nível do 'src/'

# Caminho para a pasta de assets
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# Carregando imagens
background_image = pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'backgrounds', 'background.png')))
pipe_image = pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'pipes', 'pipe.png')))
base_image = pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'base', 'base.png')))
bird_image = [
    pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'bird', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'bird', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'bird', 'bird3.png')))
    ]

#Importando a fonte
pygame.font.init()
score_font = pygame.font.SysFont(config.font_style, config.font_size)

def drawscreen(screen, birds, pipes, base, score):
    
    # Desenhando o fundo
    screen.blit(background_image, (0, 0))
    
    # Desenhando as aves
    for bird in birds:
        bird.draw(screen)
        
    # Desenhando as tubulações
    for pipe in pipes:
        pipe.draw(screen)
        
    # Desenhando a base
    base.draw(screen)
        
    # Desenhando a pontuação
    text = score_font.render(str(score), True, (255, 255, 255))
    screen.blit(text, (config.SCREEN_WIDTH - 10 - text.get_width(), 10))
    
    # Atualizando a tela
    pygame.display.update()
        
def main():
    birds = [
        libbird.Bird(
            x=config.bird_position_x,
            y=config.bird_position_y,
            images=bird_image,
            jump_speed=config.bird_jump_speed,
            rotation_max=config.bird_rotation_max,
            rotation_min=config.bird_rotation_min,
            rotation_speed=config.bird_rotation_speed,
            animation_duration=config.bird_animation_duration,
            acceleration=config.bird_acceleration
            )]
    
    pipes = [
        libpipe.Pipe(
            x=config.pipe_x_distance + 100,
            pipe_y_distance=config.pipe_y_distance,
            pipe_speed=config.pipe_speed,
            base_pipe_image=pipe_image,
            pipe_height_max=config.pipe_height_max,
            pipe_height_min=config.pipe_height_min
            )
    ]
    
    base = libbase.Base(
        y = config.base_y,
        base_image = base_image,
        base_speed = config.base_speed
        )
    
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    score = 0
    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(config.fps)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for bird in birds:
                    bird.jump()

        for bird in birds:
            bird.move()
        base.move()
        
        remove_pipes = []
        add_pipe = False
        
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.colide(bird):
                    birds.pop(i)
                if not pipe.passed and config.bird_position_x > pipe.x:
                    score += 1        
            if not pipe.passed and config.bird_position_x > pipe.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()
            if pipe.x + pipe.top_pipe_image.get_width() < 0:
                remove_pipes.append(pipe)
        
        if add_pipe:
            pipes.append(libpipe.Pipe(
            x=config.pipe_x_distance,
            pipe_y_distance=config.pipe_y_distance,
            pipe_speed=config.pipe_speed,
            base_pipe_image=pipe_image,
            pipe_height_max=config.pipe_height_max,
            pipe_height_min=config.pipe_height_min
            )) 
        if remove_pipes:
            for pipe in remove_pipes:
                pipes.remove(pipe)

        for i, bird in enumerate(birds):
            if bird.y + bird.image_height > base.y or bird.y < 0:
                birds.pop(i)
        
        
        drawscreen(screen=screen, birds=birds, pipes=pipes, base=base, score=score)
        
if __name__ == '__main__':
    main()