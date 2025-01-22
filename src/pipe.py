import pygame
import random

class Pipe:
    def __init__(self, x, pipe_between_distance, pipe_speed, base_pipe_image, pipe_hight_max, pipe_hight_min):
        self.x = x
        self.pipe_between_distance = pipe_between_distance
        self.pipe_speed = pipe_speed
        self.hight = 0
        self.pos_top = 0
        self.pos_base = 0
        self.top_pipe_image = pygame.transform.flip(base_pipe_image, False, True)
        self.base_pipe_image = base_pipe_image
        self.passed = False
        self.pipe_hight_max = pipe_hight_max
        self.pipe_hight_min = pipe_hight_min 
        self.define_hight()
        
        
    def define_hight(self):
        self.hight=random.randrange(self.pipe_hight_max, self.pipe_hight_min)
        self.pos_top = self.hight - self.top_pipe_image.get_hight()
        self.pos_base = self.hight + self.pipe_between_distance
    
    def move(self):
        self.x -= self.pipe_speed
        
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


