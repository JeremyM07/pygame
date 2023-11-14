import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
     
        self.rect = self.image.get_rect()

class Alien(Block):

    def __init__(self,color,width,height,xPos,yPos):
        super().__init__(color,width,height)

        self.xPos = xPos
        self.yPos = yPos
    
    def movementRow(self):

        restart = False
        while xPos < 700 and yPos == 35:
            yield [xPos,0]
            xPos += 1
        while xPos > 700 and yPos < 85:
            yield [0,yPos]
            yPos += 1
        while xPos > 0 and yPos == 85:
            yield [xPos,0]
            xPos -= 1
        while xPos == 0 and yPos < 135:
            yield [0,yPos]
            yPos += 1
        while xPos <700 and yPos == 135:
            yield [xPos,0]
            xPos += 1
        xPos = -10
        yPos = 35
        restart = True
        while xPos < 35 and yPos == 35 and restart:
            xPos += 1
            yield [xPos,0]
            if xPos == 35:
                restart = False
        self.movementRow()
        
        

        
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
alien_list = pygame.sprite.Group()
blockers_list = pygame.sprite.Group()
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
blockX = 35
blockY = 35

for i in range(5):
    # This represents a block
    block = Alien(GREEN, 20, 20,blockX,blockY)

    
    # block.rect.x = blockX
    # block.rect.y = blockY
 
    # Add the block to the list of objects
    alien_list.add(block)
    all_sprites_list.add(block)
    blockX+= 138
blockY+=50
blockX = 100
for i in range(4):
    # This represents a block
    block = Alien(GREEN, 20,blockX,blockY)

    
    # block.rect.x = blockX
    # block.rect.y = blockY
 
    # Add the block to the list of objects
    alien_list.add(block)
    all_sprites_list.add(block)
    blockX+= 138
blockX = 35
blockY += 50
for i in range(5):
    # This represents a block
    block = Alien(GREEN, 20, 20,blockX,blockY)

    
    # block.rect.x = blockX
    # block.rect.y = blockY
 
    # Add the block to the list of objects
    alien_list.add(block)
    all_sprites_list.add(block)
    blockX+= 138

blockerX = 25
blockerY = 300
for i in range(3):
    blocker = Block(BLUE,45,21)

    blocker.rect.x = blockerX
    blocker.rect.y = blockerY

    blockers_list.add(blocker)
    all_sprites_list.add(blocker)

    blockerX+= 275
# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    # Clear the screen
    screen.fill(BLACK)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    if pos[0] <= 680:
        player.rect.x = pos[0]
    player.rect.y = 380

    block.rect.x = block.movementRow()[0]
    block.rect.y = block.movementRow()[1]
    
 
    
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()