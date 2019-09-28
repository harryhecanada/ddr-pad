import os, pygame, sys
from pygame.locals import *
from enum import IntEnum

class KeyMapping(IntEnum):
  LEFT = 0
  DOWN = 1
  UP = 2
  RIGHT = 3
  TRIANGLE = 4
  SQUARE = 5
  X = 6
  O = 7
  SELECT = 8
  START = 9

combination_set = {KeyMapping.LEFT, KeyMapping.RIGHT, KeyMapping.UP, KeyMapping.DOWN}
key_image = 'key.png'
background_image = 'blank.png'

def main():
  # init
  pygame.init()

  # look for joysticks
  totaljoy = pygame.joystick.get_count()
  print(totaljoy,"joysticks total -")

  if totaljoy < 1:
    print('no joysticks found.')
    sys.exit()

  ddrmat = pygame.joystick.Joystick(totaljoy-1)
  ddrmat.init()
  print ("last one is",ddrmat.get_numaxes(),"axes and",ddrmat.get_numbuttons(),"buttons")
  
  # set up the screen and all that stuff
  screen = pygame.display.set_mode((1920, 1080), FULLSCREEN|HWSURFACE|DOUBLEBUF) 
  pygame.display.set_caption('pyDDR')
  pygame.mouse.set_visible(1)

  # load images
  key = pygame.image.load(key_image).convert()
  background = pygame.image.load(background_image).convert()
  
  down_buttons = set()
  
  while True: 
    
    event = pygame.event.poll()
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
        break

    if event.type == JOYBUTTONDOWN:
      down_buttons.add(event.button)
      if combination_set == down_buttons:
        screen.blit(key, (0, 0))
        pygame.display.flip()
        
    if event.type == JOYBUTTONUP:
      down_buttons.remove(event.button)
      if combination_set != down_buttons:
        screen.blit(background, (0, 0))
        pygame.display.flip()

    
if __name__ == '__main__': 
  main()