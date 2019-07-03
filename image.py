import numpy as np
import cv2
from matplotlib import pyplot as plt

def log(input_image):
    
    img00 = np.uint8(5*np.log1p(img))
    img2 = cv2.normalize(img00, img, 0, 255, cv2.NORM_MINMAX, dtype = cv2.CV_8U)
    cv2.imshow('image',img2)
    
    
def power(input_image):
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, 0.4) * 255.0, 0, 255)
    res = cv2.LUT(input_image, lookUpTable)
    cv2.imshow('image',res)

img = cv2.imread('k2.jpg',255)
log(img)
#power(img)
plt.hist(img.ravel(),256,[0,256]); plt.show()

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
