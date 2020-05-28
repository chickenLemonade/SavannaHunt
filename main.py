import pygame
import random

pygame.init()

# makes screen info
screen_info = pygame.display.Info()

# set size of game board to screen size
screen_size = (width, height) = (screen_info.current_w, screen_info.current_h)

# set screen to screen size
screen = pygame.display.set_mode(screen_size)

#color of background
color = (235, 204, 52)

# loading the prey image
prey_image = pygame.image.load("prey.jpg")
prey_image = pygame.transform.smoothscale(prey_image, (100, 100))

prey_rect = prey_image.get_rect()

# places image
prey_rect.center = (width//2, height//2)

#variables to move prey
speed = pygame.math.Vector2(30, 5)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)

pygame.transform.rotate(prey_image, 180 - rotation)


# game code
def main():
  #while true == will always run
  while True:
    
    #makes background color
    screen.fill(color)

    #updates it
    pygame.display.flip()



#game loop
if __name__ == '__main__':
  main() 