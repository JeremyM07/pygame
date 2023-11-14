import pygame

import math

pygame.init()

 

# Define some colors

BLACK    = (   0,   0,   0)

WHITE    = ( 255, 255, 255)

GREEN    = (   0, 255,   0)

RED      = ( 153,   0,   0)

blue    =   0,   205, 255

YELLOW = (255, 255, 0)

blue =list(blue)

BROWN = (102, 51, 0)

LIGHT_BROWN = (153, 76, 0)

 

# Loop until the user clicks the close button.

done = False

 

# Used to manage how fast the screen updates

clock = pygame.time.Clock()

 

size = (700, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Jeremy's Barnhouse")

# Loop until the user clicks the close button.

done = False

 

# Used to manage how fast the screen updates

clock = pygame.time.Clock()

#Global Variables

 

x_val = 10

y_val = 10
rec1y = 100
rec2y = 100
xOffset = 5
yOffset = 5

# -------- Main Program Loop -----------

while not done:

    # --- Main event loop

    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close

            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_DOWN:
                rec1y -= 10
            elif event.type == pygame.K_UP:
                rec1y += 10
            if event.type == pygame.K_w:
                rec2y += 10
            elif event.type == pygame.K_s:
                rec2y -= 10

 

    # --- Game logic should go here
    # if event.type == pygame.K_DOWN:
    #     rec1y -= 10
    # if event.type == pygame.K_UP:
    #     rec1y += 10
    # if event.type == pygame.K_w:
    #     rec2y += 10
    # if event.type == pygame.K_s:
    #     rec2y -= 10

    if x_val>=675 or x_val<= 0:
        xOffset *= -1
    if y_val<=0 or y_val>=475:
        yOffset *= -1

    x_val += xOffset

    y_val += yOffset

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    screen.fill(blue)
    # above this, or they will be erased with this command.


    #Draw here
    pygame.draw.circle(screen, YELLOW, [x_val, y_val], 25)
    pygame.draw.rect(screen,BROWN, [680,rec1y,20,100])
    pygame.draw.rect(screen,BROWN, [0,rec2y,20,100])

    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

   

    # --- Limit to 60 frames per second

    clock.tick(60)

 #end while

 

pygame.quit()