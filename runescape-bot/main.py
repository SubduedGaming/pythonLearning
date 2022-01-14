import pyautogui as pt 
from time import sleep
import cv2 as cv

pt.FAILSAFE = True
mouseDuration = 2 # Mouse move time (Seconds)

def findOnScreen(findImage): #click, numClick):
    postition = pt.locateOnScreen(findImage, grayscale=True, confidence=.5)
    
    print(postition)
 
 
sleep(5)
image = 'images/playNow.png'
findOnScreen(image)