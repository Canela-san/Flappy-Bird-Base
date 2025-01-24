class Base:
    def __init__(self, position_y, base_image, speed):
        self.y = position_y
        self.image = base_image
        self.speed = speed
        self.width = base_image.get_width()
        self.x1 = 0
        self.x2 = self.width
        
    def move(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        
        if self.x1 < -self.width:
            self.x1 += 2 * self.width
        elif self.x2 < -self.width:
            self.x2 += 2 * self.width

    def draw(self, screen):
        screen.blit(self.image, (self.x1, self.y))
        screen.blit(self.image, (self.x2, self.y))
        