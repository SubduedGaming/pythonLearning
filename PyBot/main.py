import cv2 as cv
import numpy as np 
import pyautogui

threshold = 0.85

eve_station_img = cv.imread('eve-screenshot.jpg', cv.IMREAD_UNCHANGED)
undock = cv.imread('undock-button.jpg', cv.IMREAD_UNCHANGED)

search = cv.matchTemplate(eve_station_img, undock, cv.TM_CCOEFF_NORMED)


#Getting best match location
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(search)


if max_val > threshold:
    print("found your button ")
else:
    print("Sorry match not found. ")