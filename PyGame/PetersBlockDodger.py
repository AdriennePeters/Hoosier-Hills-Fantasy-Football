import pygame 
import time 
import random 
import sys
pygame.init()
#add variable for the width and height of the display surface
display_width = 800
display_height = 600
#set up window and its size
gameDisplay = pygame.display.set_mode((display_width,display_height))
#Add color definitions(for  future games)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
block_color = (53,115,255)
#set the car width 
car_width = 112
pygame.display.set_caption('A little race car')
#define the clock 
clock = pygame.time.Clock()
#load the car image into the image buffer (see comments after the program)
carImg = pygame.image.load('carTrans.png')
'''Things Dodged Function'''
def things_dodged(count):
   font = pygame.font.SysFont(None,26)
   text = font.render('Dodged:'+str(count),True,black)
   gameDisplay.blit(text(5,5))
'''Thing Function'''
def things(thingx, thingy, thingw, thingh,color):
   pygame.draw.rect(gameDisplay,block_color,[thingx,thingy,thingw,thingh])
#Add the car's bilt function. To "bilt" is to move the car from the buffer to the
#surface, where it can be seen
'''Car Function'''
def car(x,y):
   gameDisplay.blit(carImg,(x,y))
'''Text_Objects Function'''
def text_objects(text,font):
    #The parameter True below is for antialiasing - reduces jaggyness of a shapes 
    #edge's
    #see - https://nerdtechy.com/what-is-anti-aliasing
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
'''Message_Display Function'''
def message_display(text):
   #largeText = pygame.font.Font('freesansbold.tff',115) did not work
   largeText = pygame.font.SysFont('comicsnansms',115)
   #return the text surface and the text rectangle
   TextSurf, TextRect = text_objects(text,largeText)
   #center the text
   TextRect.center = ((display_width/2),(display_height/2))
   #blit the text to the screen 
   gameDisplay.blit(TextSurf, TextRect)
   pygame.display.update()
   #keep this messae on the screen for 2 seconds
   time.sleep(2)
   #start the game over by calling game_loop()
'''Crash Function'''
def crash():
   message_display('You Crashed!')
'''Game_Loop Function '''
def game_loop():
   #define the starting location of the car
   x = (display_width*.45)
   y = (display_height*.52)
   #Make the game loop, the logic for your game
   gameExit = False
   #x_change is the amount by which the car moves left or right when the arrow is pushed
   x_change = 0
   thing_startx = random.randrange(0,display_width)
   thing_starty = -600
   thing_speed = 3
   thing_width = 100
   thing_height = 100
   dodged = 0
   while not gameExit:
      #pygame.event creates a list of events that have happened 
      for event in pygame.event.get():
         #pygame.QUIT happend when a window is closed
         if event.type == pygame.QUIT:
            gameExit = True
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               x_change = -5 
            elif event.key == pygame.K_RIGHT:
               x_change = 5
         if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               x_change = 0
      #Update the x position of the car
      x+=x_change
      #Erase the drawing surface
      gameDisplay.fill(white)
      #create a rectangular object by calling the things function
      things(thing_startx, thing_starty, thing_width, thing_height, block_color)
      thing_starty += thing_speed
      #draw the car by calling the function car()
      car(x,y)
      #Test to see if car goes off the screen 
      if x>display_width-car_width or x<0:
         #The next line will be changed late - used now for testing boundary 
         crash()
      #See if block is off the bottom of the screen 
      if thing_starty > display_height:
         thing_starty = 0-thing_height#puts the block above y = 0
         thing_startx = random.randrange(0,display_width)
         dodged +=1
         thing_speed+=1
         thing_width += dodged*1.3
      #see if the car crashed into a block
      if y<thing_starty + thing_height:
         print('y crossover')
         #the first part of the OR checks to see if the left side of the car 
         #collides with the block, and the second part of the OR checks to see
         #if the right side of the car colides wth the block
         if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
            print('x crossover')
            crash()
      #update the display
      pygame.display.update()
      #define frames per second 
      clock.tick(60)#60 frames per second
#Call the game loop
game_loop()
#Quit
pygame.quit()
quit()

'''Here a brief description of an image buffer.

In order for a program to do work on something, it (usually) has to be in memory. 
If a program is going to do work on an image - maybe creating an image or modifying
an image - it allocates memory to hold the image while it works on it. 
That allocated memory is then referred to as an image buffer. (If it was going to 
work on audio, the allocated memory would be called an audio buffer, etc.)'''