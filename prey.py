import pygame
import random
from pygame.locals import *

# makes class for prey

class Prey(pygame.sprite.Sprite):
  def __init__(self, pos):
    #loads image
    self.image = pygame.image.load("prey.jpg")   
    # gets a random size     
    scale = random.randint(3, 7)*10        
    self.image = pygame.transform.smoothscale(self.image, (scale, scale))        
    self.rect = self.image.get_rect()  
    # puts the image where you clicked      
    self.rect.center = pos
    # sets speed
    self.speed = pygame.math.Vector2(0, random.randint(2, 5))
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
        screen.blit(self.image, self.rect)