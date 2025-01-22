import pygame
import os
import random

import pygame.display
import config
import bird
import pipe
import base



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
        bird.Bird(
            x=config.bird_position_x,
            y=config.bird_position_y,
            images=bird_image,
            jump_speed=config.bird_jump_speed,
            rotation_max=config.bird_rotation_max,
            rotation_speed=config.bird_rotation_speed,
            animation_duration=config.bird_animation_duration,
            acceleration=config.bird_acceleration
            )]
    
    pipes = [
        pipe.Pipe(
            x=config.pipe_position_x,
            pipe_between_distance=config.pipe_between_distance,
            pipe_speed=config.pipe_speed,
            base_pipe_image=pipe_image,
            pipe_hight_max=config.pipe_hight_max,
            pipe_hight_min=config.pipe_hight_min
            )
    ]
    
    base = base.Base(
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
        drawscreen(screen=screen, birds=birds, pipes=pipes, base=base, score=score)
        
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
        
        add_pipe = False
        for pipe in pipes:
            pipe.move()
        