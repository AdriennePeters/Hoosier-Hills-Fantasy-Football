#KccSMUPS_3
import pygame
import random

WIDTH = 600
HEIGHT = 800
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")#Shmup is short for "shoot them up."
clock = pygame.time.Clock()

#Define Player as a sublass of the Sprite class.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Create a surface on which to draw the player
        self.image = pygame.Surface((112, 75))
        #For now the player will be a green rectangle.  Later this will
        #be an image.        
        self.image = pygame.image.load('playerShip2_orange.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        #Create or "spawn" a new bullet.
        #Put the bottom of the bullet at the top of the player
        bullet = Bullet(self.rect.centerx, self.rect.top)
        #Add the bullet to all sprites
        all_sprites.add(bullet)
        #Add the bullet to the bullets group
        bullets.add(bullet)
        
#Define Mob as a sublass of the Sprite class.
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #Create a surface on which to draw a Mob object
        self.image = pygame.Surface((89, 82))
        #For now the a Mob object wil be a red rectangle.  Later this will
        #be an image.         
        self.image = pygame.image.load('meteorGrey_big3.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


#Define Bullet as a subclass of Sprite
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #Create a surface on which to draw a Bullet object
        self.image = pygame.Surface((13, 54))
        #For now the a Bullet object will be a yellow rectangle.  
        self.image = pygame.image.load('laserGreen10.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

#Create 3 groups
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            #Fires a bullte by calling the player's shoot() function.
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()
    
    #Check to see if a mob and a bullet collide
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    #Respawn any mob that was deleted, so that we won't run out of mobs to quickly
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    #Check to see if a mob hit a player - The boolean parameter False
    #means not to delete a mob when it hits the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    #If hits: checks to see if any mobs are in the list
    if hits:
        running = False

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()