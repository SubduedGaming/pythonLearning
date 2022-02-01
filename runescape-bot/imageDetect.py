import cv2 as cv
import numpy as np

#import sys
#sys.path.append('C:\Users/georg/AppData/Local/Programs\Python\Python310\Lib\site-packages')

needle_img = cv.imread('images/playNow.png', cv.IMREAD_UNCHANGED)
haystack_img = cv.imread('images/haystack.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

# Gets the best match
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

if max_val >= 0.8:
    print("Found needle...")
    
    #get dimesions of needle img
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
    
    cv.rectangle(haystack_img, top_left, bottom_right, 
                 color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    
    
else:
    print("Needle not found!")
    
cv.imshow('Result', haystack_img)
cv.waitKey()