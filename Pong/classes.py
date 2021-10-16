import pygame
from random import randint

# Colours
Black = (0,0,0)
White = (255,255,255)

class Paddle(pygame.sprite.Sprite):
    # Class represents a paddle. foundations from sprite class
    
    def __init__(self, colour, width, height):
        # call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass paddle colour, and its X and Y posistion, width and height.
        # Set backgroud colour, and set it to transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(Black)
        self.image.set_colorkey(Black)
        
        # Draw the Paddle (A Rectangle)
        pygame.draw.rect(self.image, colour, [0, 0, width, height])
        
        # Fetch Rectangle
        self.rect = self.image.get_rect()
        
    def moveUp(self, pixels):
        self.rect.y -= pixels
        # check you're not going off the screen
        if self.rect.y < 0:
            self.rect.y = 0
    
    def moveDown(self, pixels):
        self.rect.y += pixels
        # check you're not going off the screen
        if self.rect.y > 400:
            self.rect.y = 400
            
class Ball(pygame.sprite.Sprite):
    # Rep a ball, derived from sprite constructor
    
    def __init__(self, colour, width, height):
        super().__init__()
        
        #pass ball colour, width and height
        self.image = pygame.Surface([width, height])
        self.image.fill(Black)
        self.image.set_colorkey(Black)
        
        # Draw the ball (Reactangle)
        pygame.draw.rect(self.image, colour, [0, 0, width, height])
        
        self.velocity = [randint(4,8), randint(-8,8)]
        
        # Fetch the rectangle object with dimesions of image
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)