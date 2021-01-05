import cv2 as cv 
import numpy as np 
import pyautogui
from time import time

screenshot = pyautogui.screenshot()
screenshot = np.array(screenshot)


cv.imshow('screenshot', screenshot)
cv.waitKey()