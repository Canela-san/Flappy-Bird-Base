class Base:
    def __init__(self, y, base_image, base_speed):
        self.y = y
        self.base_image = base_image
        self.base_speed = base_speed
        self.width = base_image.get_width()
        self.x1 = 0
        self.x2 = self.width
        
    def move(self):
        self.x1 -= self.base_speed
        self.x2 -= self.base_speed
        
        if self.x1 < -self.width:
            self.x1 += 2 * self.width
        elif self.x2 < -self.width:
            self.x2 += 2 * self.width

    def draw(self, screen):
        screen.blit(self.base_image, (self.x1, self.y))
        screen.blit(self.base_image, (self.x2, self.y))
        