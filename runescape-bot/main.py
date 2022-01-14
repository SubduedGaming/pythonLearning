import pyautogui as pt 
from time import sleep
import cv2 as cv

pt.FAILSAFE = True
mouseDuration = 2 # Mouse move time (Seconds)

def findOnScreen(findImage): #click, numClick):
    postition = pt.locateCenterOnScreen(findImage, confidence=.3)
    sleep(1)
    pt.moveTo(postition)
    #print(postition, mouseDuration)
    sleep(1)
 
 
sleep(5)
image = 'images/playNow.png'
findOnScreen(image)