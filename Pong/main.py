import pygame
from classes import Paddle
from classes import Ball

pygame.init()

# Colours
Black = (0,0,0)
White = (255,255,255)

# Size of Screen
Size = (700, 500)
Screen = pygame.display.set_mode(Size)
pygame.display.set_caption("Pong with AI")

# Making Objects
paddleA = Paddle(White, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB= Paddle(White, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(White, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# This list contains all the sprites we will use
all_sprites_list = pygame.sprite.Group()

# Add paddles to the list
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# Game will continue to run until user exit's the game
carryOn = True

# Clock to tell game how many fps to run at
Clock = pygame.time.Clock()

# Player scores
playerA = 0
playerB = 0

# Main Loop
while carryOn:
    #Main event loop
    for event in pygame.event.get(): # User Did Something
        if event.type == pygame.QUIT: # If user exits game change 'carryOn' to False
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x: # Pressing 'x' will exit game.
                carryOn = False            

    # Moving paddles code goes here
    pixelToMove = 10
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(pixelToMove)
    if keys[pygame.K_s]:
        paddleA.moveDown(pixelToMove)
    if keys[pygame.K_UP]:
        paddleB.moveUp(pixelToMove)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(pixelToMove)
    
    # Game Logic Here
    all_sprites_list.update()
    
    # Check if ball is bouncing against walls
    if ball.rect.x >= 690:
        ball.velocity[0] = -ball.velocity[0]
        playerA += 1
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
        playerB += 1
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]
    
    # Detect collisions
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
    
    # Drawing code here
    # Clear Screen to Black
    Screen.fill(Black)
    # Draw the net
    pygame.draw.line(Screen, White, [349,0], [349, 500], 5)
    
    # Draw all sprites
    all_sprites_list.draw(Screen)
    
    # Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(playerA), 1, White)
    Screen.blit(text, (250,10))
    text = font.render(str(playerB), 1, White)
    Screen.blit(text, (420,10))
    
    # Update screen
    pygame.display.flip()
    
    # tick speed
    Clock.tick(60)
    
# Stop game engine
pygame.quit()
print(playerA)
print(playerB)