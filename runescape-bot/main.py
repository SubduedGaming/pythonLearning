import pyautogui as pt 
from time import sleep
import cv2 as cv

pt.FAILSAFE = True
mouseDuration = 2 # Mouse move time (Seconds)

def findOnScreen(findImage): #click, numClick):
    postition = pt.locateCenterOnScreen(findImage)
    
    print(postition)
 
 
sleep(1)   
findOnScreen('menuButton.jpg')