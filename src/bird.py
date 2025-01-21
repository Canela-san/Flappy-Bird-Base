class Bird:
    def __init__(self, x, y, images, jump_speed, transform_size, rotation_max, rotation_speed, animation_duration, acceleration):
        self.x = x
        self.y = y
        self.images = images
        self.jump_speed = jump_speed
        self.transform_size = transform_size
        self.rotation_max = rotation_max
        self.rotation_speed = rotation_speed
        self.animation_duration = animation_duration
        self.acceleration = acceleration
        self.current_image = images[0]
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

    def draw(self):
        # definir qual imagem do passaro vai usar
        # se o pássaro estiver caindo não bate asa
        # desenhar
        pass


