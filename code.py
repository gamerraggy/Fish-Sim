import pygame
import random
import time


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fish Simulator")
clock = pygame.time.Clock() 

class Fish:
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
        if self.xpos <= -75:
            self.xpos = 870
        if self.ypos <= 0 or self.ypos>= 550:
            self.ypos = 300

    def draw(self, screen):
        screen.blit(self.fishImage, (self.xpos, self.ypos))

# instantiate a fish object
fish = Fish()


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
    # Fill the screen with a background color
    screen.fill((0, 150, 255))

    # Draw the fish
    fish.draw(screen)

    # Update the display
    pygame.display.flip()

    #end of game loop!#######################################################

pygame.quit()
