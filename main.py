import pygame
import random
from pygame.locals import *
from prey import *
from lion import *
from hunter import *

#reactions possible for catching prey
eat = ['Delicious!', 'Mmmm', 'Tasty', 'I\'ve caught you!', 'You\'ll never escape!', 'You will make a fine dinner']

#when hunter touches lion
hurt = ['Ahh!', 'That hurt!', 'You are a BAD hunter!', 'Please don\'t hurt me!', 'Ouch!']

# react = random.randint(0, len(die) - 1)
# dieReaction = die[react]

#when hunter kills lion
die = ['Nooooooo', 'Why?', 'I have a family!']

# start score
scorePoint = 0

# start health
hp = 20

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

#color of background when you win
newColor = (66,103,149)

#color of background when you die
dieColor = (228,89,69)

#tect color and background color
textColor=(50,254,30)
txtBackgroundColor=(94,0,4)

#stuff for the score
scoreColor = (184,240,161)
scoreBackground = (7,84,152)

#color of win text
winColor = (152,195,225)
winBackgroundColor = (66,103,149)

#color of die text
deathColor = (223,245,128)
deathBackgroundColor = (228,89,69)

#color of hurt text
ouchColor = (244,201,12)
ouchBack = (140,219,246)

#stuff for hp
hpColor = (184,240,161)
hpBackgroundColor = (7,84,152)

player = Lion((150,180))

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

#hunters created
hunters = pygame.sprite.Group()

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
    global scorePoint
    global scoreAPoint
    global hp
    global myHp
    myHp = ("Health is: " + str(hp))
    scoreAPoint = ("Score is: " + str(scorePoint))

    for event in pygame.event.get():
      if event.type == quit:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        # determines if hunter spawns
        num = random.randint(0, 1234)
        if num % 2 == 0:
          hunters.add(Hunter(event.pos))
        else:
          #adds prey
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

    move_prey()
    #makes background color
    screen.fill(color)
    screen.blit(prey_image, prey_rect)

    for prey in preys:
      prey.update()
    for prey in preys:
      prey.draw(screen)

    for hunter in hunters:
      hunter.update()
    for hunter in hunters:
      hunter.draw(screen)

    screen.blit(player.image,player.rect)
    player.update()

    hit_hunter = pygame.sprite.spritecollide(player,hunters,True)
    screen.blit(player.image,player.rect)
    if hit_hunter:
      #picks a reaction
      getHurt = random.randint(0, len(hurt) -1)
      hurtReaction = hurt[getHurt]

      font = pygame.font.Font('freesansbold.ttf', 32) 
      ouch = font.render(hurtReaction, True, ouchColor, ouchBack)
      ouchRect = ouch.get_rect() 
      ouchRect.center = (width // 2, 550)
      screen.blit(ouch,ouchRect)

      hp = hp -1

    get_hit=pygame.sprite.spritecollide(player,preys,True)
    screen.blit(player.image,player.rect)
    if get_hit:
      # picks a reaction
      num = random.randint(0, len(eat) - 1)
      devour = eat[num]

      #stuff for font
      font = pygame.font.Font('freesansbold.ttf', 32) 
      text = font.render(devour, True, textColor, txtBackgroundColor)
      textRect = text.get_rect() 
      textRect.center = (width // 2, 550)
      screen.blit(text,textRect)

      #adds a to the score point every time
      scorePoint += 1
      
    #same as text
    scoreFont = pygame.font.Font('freesansbold.ttf', 32) 
    score = scoreFont.render(scoreAPoint, True, scoreColor, scoreBackground)
    scoreRect = score.get_rect() 
    scoreRect.topleft = (50, 90)
    screen.blit(score,scoreRect)

    hpFont = pygame.font.Font('freesansbold.ttf', 32) 
    theHp = hpFont.render(myHp, True, hpColor, hpBackgroundColor)
    hpRect = theHp.get_rect() 
    hpRect.topleft = (50, 50)
    screen.blit(theHp,hpRect)

    if scorePoint >= 30:
      screen.fill(newColor)

      winFont = pygame.font.Font('Modak-Devanagari.ttf', 100) 
      win = winFont.render("You won!!!", True, winColor, winBackgroundColor)
      winRect = win.get_rect() 
      winRect.center = (width // 2, height //2)
      screen.blit(win,winRect)
    
    if hp <= 0:
      screen.fill(dieColor)

      dieFont = pygame.font.Font('Modak-Devanagari.ttf', 100) 
      death = dieFont.render("nooooo", True, deathColor, deathBackgroundColor)
      dieRect = death.get_rect() 
      dieRect.center = (width // 2, height //2)
      screen.blit(death,dieRect)
      

    #updates it
    pygame.display.flip()


#game loop
if __name__ == '__main__':
  main() 