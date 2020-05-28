import pygame, random

# class to create lion
class Lion(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        #loads image
        self.image = pygame.image.load('lion.jpg')
        self.image = pygame.transform.smoothscale(self.image, (100, 100))
        
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, 0)

    def update(self):
        screen_info = pygame.display.Info()
        self.rect.move_ip(self.speed)
        #if it hits the left or right side, deflect
        if self.rect.left < 0 or self.rect.right > screen_info.current_w:
            self.speed[0] *= -1
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.move_ip(self.speed[0], 0)
        #if it hits the top or bottom, delfect
        if self.rect.top < 0 or self.rect.bottom > screen_info.current_h:
            self.speed[1] *= -1
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.move_ip(0, self.speed[1])

    def checkReset(self, endPos):
        return self.rect.center[0] > endPos

    def reset(self, pos):
        self.rect.center = pos