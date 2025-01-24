import pygame
import random

class Pipe:
    def __init__(self, x_distance, y_distance, speed, base_pipe_image, height_max, height_min):
        self.x = x_distance
        self.y_distance = y_distance
        self.speed = speed
        self.height = 0
        self.pos_top = 0
        self.pos_base = 0
        self.top_pipe_image = pygame.transform.flip(base_pipe_image, False, True)
        self.base_pipe_image = base_pipe_image
        self.passed = False
        self.height_max = height_max
        self.height_min = height_min 
        self.define_height()
        
        
    def define_height(self):
        self.height=random.randrange(self.height_max, self.height_min)
        self.pos_top = self.height - self.top_pipe_image.get_height()
        self.pos_base = self.height + self.y_distance
    
    def move(self):
        self.x -= self.speed
        
    def draw(self, screen):
        screen.blit(self.top_pipe_image, (self.x, self.pos_top))
        screen.blit(self.base_pipe_image, (self.x, self.pos_base))
        
    def colide(self, bird):
        bird_mask = bird.get_mask()
        
        top_pipe_mask = pygame.mask.from_surface(self.top_pipe_image)
        base_pipe_mask = pygame.mask.from_surface(self.base_pipe_image)
        
        top_distance = (self.x - bird.x, self.pos_top - round(bird.y))
        base_distance = (self.x - bird.x, self.pos_base - round(bird.y))
        
        colision_top_point = bird_mask.overlap(top_pipe_mask, top_distance)
        colision_base_point = bird_mask.overlap(base_pipe_mask, base_distance)
       
        if colision_top_point or colision_base_point:
            return True
        else:
            return False


