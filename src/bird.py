import pygame
class Bird:
    def __init__(self, x, y, images, jump_speed, rotation_max, rotation_speed, animation_duration, acceleration):
        self.x = x
        self.y = y
        self.images = images
        self.jump_speed = jump_speed
        self.rotation_max = rotation_max
        self.rotation_speed = rotation_speed
        self.animation_duration = animation_duration
        self.acceleration = acceleration
        self.current_image = images[0]
        self.image_count = 0
        self.angle = 0
        self.speed = 0
        self.hight = self.y
        self.time = 0
        
    def jump(self):
        self.speed = self.jump_speed
        self.hight = self.y
        self.time = 0
        
    def move(self):
        # calcular deslocamento
        self.time += 1
        displacement = self.acceleration * (self.temp**2) + self.speed * self.time
        
        # restringir o deslocamento
        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2        
        self.y += displacement
            
        # calcular angulo da imagem
        if displacement < 0 or self.y < (self.hight + 50):
            if self.angle < self.rotation_max:
                self.angle = self.rotation_max
            elif self.angle > -90:
                self.angle -= self.rotation_speed

    def draw(self, screen):
        # definir qual imagem do passaro vai usar
        self.image_count += 1
        if self.image_count < self.animation_duration:
            self.current_image = self.images[0]
        elif self.image_count < self.animation_duration*2:
            self.current_image = self.images[1]
        elif self.image_count < self.animation_duration*3:
            self.current_image = self.images[2]
        elif self.image_count < self.animation_duration*4:
            self.current_image = self.images[1]
        elif self.image_count >= self.animation_duration*4 + 1:
            self.current_image = self.images[0]
            self.image_count = 0
            
        
        # se o pássaro estiver caindo não bate asa
        
        if self.angle <= -80:
            self.current_image = self.images[1]
            self.image_count = self.animation_duration*2
            
        
        # desenhar
        image = pygame.transform.rotate(self.current_image, self.angle)
        screen.blit(image, image.get_rect(center=self.current_image.get_rect(topleft=(self.x, self.y)).center).topleft)
        
    def get_mask(self):
        return pygame.mask.from_surface(self.current_image)