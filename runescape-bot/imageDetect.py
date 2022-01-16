import cv2 as cv
import numpy as np 

needle_img = cv.imread('images/playNow.png', cv.IMREAD_UNCHANGED)
haystack_img = cv.imread('images/haystack.png')