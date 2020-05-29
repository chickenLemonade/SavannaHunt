import pygame
import random
from pygame.locals import *

# makes class for hunter

class Hunter(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()

    self.createdTime = pygame.time.get_ticks()

    #loads image
    self.image = pygame.image.load("hunter.jpg")   
    # gets a random size     
    scale = random.randint(7, 12)*10        
    self.image = pygame.transform.smoothscale(self.image, (scale, scale))        
    self.rect = self.image.get_rect()  
    # puts the image where you clicked      
    self.rect.center = pos
    # sets speed
    self.speed = pygame.math.Vector2(0, random.randint(2, 15))
    rotation = random.randint(0, 360)
    self.speed.rotate_ip(rotation)        
    self.image = pygame.transform.rotate(self.image, 180 - rotation)

  def update(self):
    screen_info = pygame.display.Info()        
    self.rect.move_ip(self.speed)
    # if prey hits left or right
    if self.rect.left < 0 or self.rect.right > screen_info.current_w:            
      self.speed[0] *= -1            
      self.image = pygame.transform.flip(self.image, True, False)
      self.rect.move_ip(self.speed[0], 0)  
      
      #if prey hits top or bottom      
    if self.rect.top < 0 or self.rect.bottom > screen_info.current_h:            
      self.speed[1] *= -1            
      self.image = pygame.transform.flip(self.image, False, True)
      self.rect.move_ip(0, self.speed[1])
      
  def draw(self, screen):
    if pygame.time.get_ticks() - self.createdTime <= 10000:
      screen.blit(self.image, self.rect)