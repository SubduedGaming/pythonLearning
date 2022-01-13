import pyautogui as pt
from time import sleep
import cv2 as cv


# Helper function
def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=0.7)
    
    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=0.1)
        pt.moveRel(off_x, off_y,duration=0.1)
        pt.click(clicks=clicks, interval=0.3)
        
        

# Moves the character
# x = attack
# c = place
def move_character(key_press, duration, action='walking'):
    pt.keyDown(_press)
    
    if action == 'walking':
        print("Walking")
    elif action == 'attack':
        pt.keyDown('x')
        
    sleep(duration)
    pt.keyUp('x')
    pt.keyUp(key_press)
    
    
    
    
# Locate Lava
def locate_lava():
    position = pt.locateOnScreen('images/minecraft_lava_small.png', confidence=0.4)
    
    if position is None:
        return False
    else:
        # Move the character backwards to avoid burning to death
        move_charater('s', 2)
        print('Found lava!!!!')
        return True
    
    

#Start the game
sleep(5)    
nav_to_image('\images\minecraft_resume_button.png', 3)
