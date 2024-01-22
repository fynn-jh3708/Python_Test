import pygame, sys
from pygame.locals import *
pygame.init()

pygame.display.set_caption("Hello World!")
Screen = pygame.display.set_mode((300, 500))

xpos = 50
clock = pygame.time.Clock()

while 1:
  clock.tick(60)
  
  for event in pygame.event.get():
    if event.type == QUIT:
      sys.exit()

  pressed_keys = pygame.key.get_pressed()

  if pressed_keys[K_RIGHT] == 1:
    xpos += 1
  if pressed_keys[K_LEFT] == 1:
    xpos -= 1
  
  Screen.fill((255, 255, 255))
  pygame.draw.circle(Screen, (0, 255, 0), (xpos, 200), 20)

  pygame.display.update()