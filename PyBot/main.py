import cv2 as cv
import numpy as np 
import pyautogui


eve_station_img = cv.imread('eve-screenshot.jpg', cv.IMREAD_UNCHANGED)
undock = cv.imread('undock-button.jpg', cv.IMREAD_UNCHANGED)

search = cv.matchTemplate(eve_station_img, undock, cv.TM_CCOEFF_NORMED)

cv.imshow('results', search)