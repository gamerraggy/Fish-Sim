import pygame
import random
import time


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fish Simulator")
clock = pygame.time.Clock() 

bluefish = pygame.image.load("bluefish.png").convert_alpha()
ticker = 0
frameNum = 0

class FishR:
    def __init__(self):
        self.fishImage = bluefish
        pygame.Surface.set_colorkey (self.fishImage, [255,0,255])
        self.xpos = 0
        self.ypos = random.randint(0, 550)
        self.speed = 1
        self.xDir = 1
        self.yDir = random.randint(-1,1)
        self.last_change_time = time.time() #grab starting time
        self.frameWidth = 128
        self.frameHeight = 128
        self.frameNum = 0
  

    def move(self): 
        # Move the fish
        self.xpos += self.xDir* self.speed 

        # Check for collision with walls and change direction
        if self.xpos >= 800:
            self.xpos = -100
        if self.ypos <= 0 or self.ypos>= 550:
            self.ypos == 300

    def draw(self, screen):
        #screen.blit(self.fishImage, (self.xpos, self.ypos))
        screen.blit(bluefish, (fish.xpos, fish.ypos), (self.frameWidth*frameNum,0, self.frameWidth, self.frameHeight))

class FishL:
    def __init__(self):
        self.fishImage = pygame.image.load("fishcoolig - Copy (2).png").convert_alpha()
        pygame.Surface.set_colorkey (self.fishImage, [255,0,255])
        self.xpos = random.randint(0, 750)
        self.ypos = random.randint(0, 550)
        self.speed = 1
        self.xDir = -1
        self.yDir = random.randint(-1,1)
        self.last_change_time = time.time() #grab starting time

    def move(self): 
        # Move the fish
        self.xpos += self.xDir* self.speed 

        # Check for collision with walls and change direction
        if self.xpos <= -67:
            self.xpos = 817
        if self.ypos <= 0 or self.ypos>= 550:
            self.ypos == 300

    def draw(self, screen, frameNum):
        screen.blit(self.fishImage, (self.xpos, self.ypos))
        

# instantiate a fish object
fish = FishR()


running = True
while running:# Game loop########################################################
    clock.tick(60)
    #input/event section-----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #physics/update section--------------------------
    fish.move()


    #render section----------------------------------
    ticker+=1
    if ticker%10==0:
        frameNum+=1
    if frameNum>4:
        frameNum=0
    # Fill the screen with a background color
    screen.fill((0, 150, 255))

    # Draw the fish
    fish.draw(screen)
    

    # Update the display
    pygame.display.flip()

    #end of game loop!#######################################################

pygame.quit()
