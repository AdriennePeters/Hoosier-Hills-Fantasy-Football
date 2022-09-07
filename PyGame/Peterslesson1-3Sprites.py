import pygame
import random 
WIDTH = 800
HEIGHT = 600
FPS = 30
#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
class Player(pygame.sprite.Sprite):
   def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      #the convert() function converts the image into a file that pygame can 
      #manage more easily
      self.image = pygame.image.load('p1_jump.png').convert()
      self.rect = self.image.get_rect()
      self.rect.center = (WIDTH/2,HEIGHT/2)
      self.y_speed = 5
   def update(self):
      #on each iteration of the game loop, the sprite moves five to the right
      self.rect.x += 20
      self.rect.y += self.y_speed
      #next if the sprite's left side gose off the screen, place the sprite's right
      #side at 0
      if self.rect.left > WIDTH:
         self.rect.right = 0
      #create up and down motion 
      if self.rect.bottom > HEIGHT-200:
         self.y_speed = -5
      if self.rect.top < 200:
         self.y_speed = 5
#initialize pygame and create a window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#game loop
running = True
while running:
   #keep loop running at the right speed
   clock.tick(FPS)
   #process input (events)
   for event in pygame.event.get():
      #check for colsing window
      if event.type == pygame.QUIT:
         running = False
   #update
   all_sprites.update()
   #draw/render
   screen.fill(BLACK)
   all_sprites.draw(screen)
   #AFTER drawingeverything, flip the display, eg update it
   pygame.display.flip()
pygame.quit()   