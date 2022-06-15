import pygame

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load('background.png')
spaceship = pygame.image.load('spaceship.png')

keep_alive = True
clock = pygame.time.Clock()
while keep_alive:
   screen.blit(background, [0, 0])
   screen.blit(spaceship, [160, 500])
   
   pygame.display.update()
     import pygame

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load('background.png')
spaceship = pygame.image.load('spaceship.png')

keep_alive = True
clock = pygame.time.Clock()
while keep_alive:
   screen.blit(background, [0, 0])
   screen.blit(spaceship, [160, 500])
   
   pygame.display.update()
   clock.tick(60)  t