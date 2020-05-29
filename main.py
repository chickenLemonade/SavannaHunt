import pygame
import random
from pygame.locals import *
from prey import *
from lion import *

#reactions possible for catching prey
eat = ['Delicious!', 'Mmmm', 'Tasty', 'I\'ve caught you!', 'You\'ll never escape!', 'You will make a fine dinner']

scorePoint = 0
scoreAPoint = "Score is: " + str(scorePoint + 1)

pygame.init()

# Clock to set framerate
clock = pygame.time.Clock()

# makes screen info
screen_info = pygame.display.Info()

# set size of game board to screen size
screen_size = (width, height) = (screen_info.current_w, screen_info.current_h)

# set screen to screen size
screen = pygame.display.set_mode(screen_size)

#color of background
color = (235, 204, 52)

#tect color and background color
textColor=(50,254,30)
txtBackgroundColor=(94,0,4)

#stuff for the score
scoreColor = (184,240,161)
scoreBackground = (7,84,152)


player = Lion((150,150))

# loading the prey image
prey_image = pygame.image.load("prey.jpg")
prey_image = pygame.transform.smoothscale(prey_image, (100, 100))

prey_rect = prey_image.get_rect()

# places image
prey_rect.center = (width//2, height//2)

#variables to move prey
speed = pygame.math.Vector2(10, 6)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)

pygame.transform.rotate(prey_image, 180 - rotation)

#The reason it is used insetad of the array is because
#it uses a sprite, which has built in stuff that is needed
#for collision code

#prey created
preys = pygame.sprite.Group() 

#moves the prey
def move_prey():
  global prey_image
  screen_info = pygame.display.Info()
  prey_rect.move_ip(speed)

  #  IF PREY HITS TOP OR BOTTOM
  if prey_rect.top < 0 or prey_rect.bottom > screen_info.current_h:
    #go the opposite direction
    speed[1] *= -1
    prey_rect.move_ip(0, speed[1])
    #updates it
    prey_image = pygame.transform.flip(prey_image, True, False)

  #  IF PREY HITS LEFT OR RIGHT
  if prey_rect.left < 0 or prey_rect.right > screen_info.current_w:
    #go the opposite direction
    speed[0] *= -1
    prey_rect.move_ip(speed[0], 0)
    #updates it
    prey_image = pygame.transform.flip(prey_image, False, True)

# game code
def main():
  #while true == will always run
  while True:
    
    clock.tick(60)

    for event in pygame.event.get():
      if event.type == quit:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        # adds prey when and where you click
        preys.add(Prey(event.pos))
      if event.type == KEYUP:
        if event.key == K_UP:
          player.speed[1]=0 
        if event.key == K_DOWN:
          player.speed[1]=0  
        if event.key==K_LEFT:
          player.speed[0]=0
        if event.key==K_RIGHT:
          player.speed[0]=0
    if event.type == KEYDOWN:
        if event.key == K_UP:
          player.speed[1]=-15
        if event.key == K_DOWN:
          player.speed[1]=15  
        if event.key==K_LEFT:
          player.speed[0]=-15
        if event.key==K_RIGHT:
          player.speed[0]=15



        if event.key == K_g:
          speed[0] = 0
          speed[1] = 0
        if event.key == K_f:
          speed[0] = 40
          speed[1] = 40
        if event.key == K_s:
          speed[0] = 10
          speed[1] = 10



    move_prey()
    #makes background color
    screen.fill(color)
    screen.blit(prey_image, prey_rect)

    for prey in preys:
      prey.update()
    for prey in preys:
      prey.draw(screen)

    screen.blit(player.image,player.rect)
    player.update()

    get_hit=pygame.sprite.spritecollide(player,preys,False)
    screen.blit(player.image,player.rect)
    if get_hit:
      # picks a reaction
      num = random.randint(0, len(eat) - 1)
      devour = eat[num]
      #stuff for font
      font=pygame.font.Font('freesansbold.ttf', 32) 
      text = font.render(devour, True, textColor, txtBackgroundColor)
      textRect = text.get_rect() 
      textRect.center = (width // 2, height // 2)
      screen.blit(text,textRect)

      #MORE STUFF FOR THE SCORE

      #start score
      scorePoint = 0

      #adds a point every time
      scoreAPoint = "Score is: " + str(scorePoint + 1)

      #same as text
      scoreFont = pygame.font.Font('freesansbold.ttf', 32) 
      score = scoreFont.render(scoreAPoint, True, scoreColor, scoreBackground)
      scoreRect = score.get_rect() 
      scoreRect.topleft = (width // 2, height // 2)
      screen.blit(score,scoreRect)

    #updates it 
    pygame.display.flip()



#game loop
if __name__ == '__main__':
  main() 