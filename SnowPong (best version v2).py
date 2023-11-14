import pygame
import random
import time
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

pygame.display.set_caption("SnowPong")

# Loop until the user clicks the close button.

done = False

 

# Used to manage how fast the screen updates

clock = pygame.time.Clock()

#Global Variables
backgrImg = pygame.image.load("christmas(1).jpg").convert()
snowList = []
for i in range(60):
    x = random.randrange(0,700)
    y = random.randrange(0,500)
    snowList.append([x,y])
#scores
p1Score = 0
p2Score = 0
winner = 0

#text font
font = pygame.font.SysFont("Constantia",25)


# functions
def draw_text(text,font,color,x,y):
    img = font.render(text,True,color)
    screen.blit(img,(x,y))

# create player paddles
class paddle():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.rect=pygame.Rect(self.x,self.y,20,100)
        self.speed=7
    
    def movePaddle(self,playerNum):
        key = pygame.key.get_pressed()
        if playerNum == 1:
            if key[pygame.K_UP] and self.rect.top > 50:
                self.rect.move_ip(0, -1*self.speed)
            if key[pygame.K_DOWN] and self.rect.bottom < 500:
                self.rect.move_ip(0, self.speed)
        elif playerNum == 2:
            if key[pygame.K_w] and self.rect.top > 50:
                self.rect.move_ip(0, -1*self.speed)
            if key[pygame.K_s] and self.rect.bottom < 500:
                self.rect.move_ip(0, self.speed)
    
    def draw(self):
        pygame.draw.rect(screen, RED,self.rect)
        

player1Pad = paddle(660,100)
player2Pad = paddle(20,100)

#create ball
class ball():
    def __init__(self,x,y):
      self.reset(x,y)  

    def draw(self):
        pygame.draw.circle(screen,YELLOW,(self.rect.x+self.ballRadius,self.rect.y+self.ballRadius), self.ballRadius)
    def reset(self,x,y):
        self.x=x
        self.y=y
        self.ballRadius = 10
        self.rect= pygame.Rect(self.x,self.y,self.ballRadius*2,self.ballRadius*2)
        self.speedX = 4
        self.speedY = 4
        self.winner = 0#1 = player 1 scored, -1 = player 2 scored    
    def moveBall(self):

        #collision detection for top and bottom
        if self.rect.top < 60:
            self.speedY *= -1
        if self.rect.bottom > 490:
            self.speedY *= -1

        #collision with paddles
        if self.rect.colliderect(player1Pad) or self.rect.colliderect(player2Pad):
            self.speedX *= -1

        #check for point scored
        if self.rect.left < 10:
            self.winner -= 1
        if self.rect.right > 690:
            self.winner += 1



        self.rect.x+=self.speedX
        self.rect.y+=self.speedY
        return self.winner
    
pongBall = ball(350,75)
liveBall = False
speedIncrease = 0
# -------- Main Program Loop -----------

while not done:

    # --- Main event loop

    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close

            done = True # Flag that we are done so we exit this loop
        
 

    # --- Game logic should go here
   
        if event.type == pygame.MOUSEBUTTONDOWN and liveBall == False:
            liveBall = True
            speedIncrease = 0
            pongBall.reset(350,75)

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    screen.blit(backgrImg,[0,0])
    for item in snowList:
        item[1]+=1
        pygame.draw.circle(screen, WHITE,item,2)

        if item[1]>510:
            del snowList[snowList.index(item)]
            x = random.randrange(0,700)
            y = random.randrange(-2,0)
            snowList.append([x,y])

    pygame.draw.line(screen, WHITE,(0,50),(700,50))
    draw_text("Player 1: " + str(p1Score),font,WHITE,5,15)
    draw_text("Player 2: " + str(p2Score),font,WHITE,565,15)
    draw_text("Ball Speed: "+str(abs(pongBall.speedX)),font,WHITE,150,15)
    # above this, or they will be erased with this command.
    #Draw here
    player1Pad.draw()
    player2Pad.draw()
    pongBall.draw()

    if liveBall == True:
        speedIncrease += 1
        #move ball
        winner = pongBall.moveBall()
        if winner == 0:
            #move paddles
            player1Pad.movePaddle(1)
            player2Pad.movePaddle(2)
        else:
            liveBall = False
            if winner == 1:
                p1Score += 1
            elif winner == -1:
                p2Score += 1

    if liveBall == False:
        if winner == 0:
            draw_text("CLICK ANYWHERE TO START!", font, WHITE,180,180)
        if winner == 1:
            draw_text("Player 1 Scored!", font, WHITE,350,15)
            draw_text("CLICK ANYWHERE TO START!", font, WHITE,180,180)
        if winner == -1:
            draw_text("Player 2 Scored!", font, WHITE,350,15)
            draw_text("CLICK ANYWHERE TO START!", font, WHITE,180,180)

    if liveBall == True:
        if speedIncrease > 500:
            speedIncrease = 0
            if pongBall.speedX > 0:
                pongBall.speedX+=1
            if pongBall.speedX < 0:
                pongBall.speedX-=1
            if pongBall.speedY > 0:
                pongBall.speedY+=1
            if pongBall.speedY < 0:
                pongBall.speedY-=1




    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

   

    # --- Limit to 60 frames per second

    clock.tick(60)

 #end while

 

pygame.quit()