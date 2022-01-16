import pyautogui as pt 
from time import sleep
import cv2 as cv


pt.FAILSAFE = True
mouseDuration = 2 # Mouse move time (Seconds)

def findOnScreen(findImage, click): #click, numClick):
    pos = pt.locateCenterOnScreen(findImage, confidence=.8)
    sleep(1)
    if pos is None:
        print("Failed to locate image")
        break
    elif pos is not None
        if click == "left":
            pt.moveTo(pos, duration=0.5)
            sleep(.2)
            pt.click()
        if click == "right":
            pt.moveTo(pos, duration=0.5)
            sleep(.2)
            pt.click()
    
 
def main():
    sleep(3)
    image = 'images/playNow.png'
    leftClick(2, findOnScreen(image))
    
main()
    