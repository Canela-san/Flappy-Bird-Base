import pygame
class Bird:
    def __init__(self, position_x, position_y, images, jump_speed, rotation_max, rotation_min, rotation_speed, animation_duration, acceleration):
        self.x = position_x
        self.y = position_y
        self.images = images
        self.jump_speed = jump_speed
        self.rotation_max = rotation_max
        self.rotation_min = rotation_min
        self.rotation_speed = rotation_speed
        self.animation_duration = animation_duration
        self.acceleration = acceleration
        self.current_image = images[0]
        self.image_height = self.current_image.get_height()
        self.image_count = 0
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        
    def jump(self):
        self.speed = self.jump_speed
        self.height = self.y
        self.time = 0
        
    def move(self):
        # Calcular deslocamento com base no tempo
        self.time += 1
        displacement = self.acceleration * (self.time ** 2) + self.speed * self.time

        # Restringir o deslocamento máximo
        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2

        # Atualizar a posição vertical do pássaro
        self.y += displacement

        # Atualizar o ângulo de rotação da imagem
        if displacement < 0:  # Subindo
            target_angle = self.rotation_max
        else:  # Descendo
            target_angle = -90

        # Transição suave do ângulo para o alvo
        if self.angle < target_angle:
            self.angle += 10*self.rotation_speed
        elif self.angle > target_angle:
            self.angle -= self.rotation_speed

        # Garantir que o ângulo esteja dentro dos limites
        self.angle = max(min(self.angle, self.rotation_max), self.rotation_min)

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