import pygame
import os
import random
import config
import bird
import pipe
import base


# # Usando as variáveis
# SCREEN_WIDTH = config.SCREEN_WIDTH
# SCREEN_HEIGHT = config.SCREEN_HEIGHT

# Diretório base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Sobe um nível do 'src/'

# Caminho para a pasta de assets
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# Carregando imagens
background_image = pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'backgrounds', 'background.png')))
pipes_image = pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'pipes', 'pipe.png')))
base_image = pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'base', 'base.png')))
bird_image = [
    pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'bird', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'bird', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'bird', 'bird3.png')))
]

#Importando a fonte
pygame.font.init()
score_font = pygame.font.SysFont(config.font_style, config.font_size)

