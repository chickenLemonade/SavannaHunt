import pygame

pygame.init()

# makes screen info
screen_info = pygame.display.Info()

# set size of game board to screen size
screen_size = (width, height) = (screen_info.current_w, screen_info.current_h)


# set screen to screen size
screen = pygame.display.set_mode(screen_size)

#color of background
color = (235, 204, 52)

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