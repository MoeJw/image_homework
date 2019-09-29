import numpy as np
import cv2
from matplotlib import pyplot as plt
def add(input_image1,input_image2):
    img=input_image1+input_image2
    cv2.imshow('image',img)
    pass
def sub(input_image1,input_image2):
    img=input_image1-input_image2
    cv2.imshow('image',img)
    pass
def mult(input_image1,input_image2):
    img=input_image1*input_image2
    cv2.imshow('image',img)
    pass
def div(input_image1,input_image2):
    img=input_image1/input_image2
    cv2.imshow('image',img)
    pass
def log(input_image):
    
    img00 = np.uint8(5*np.log1p(img))
    img2 = cv2.normalize(img00, img, 0, 255, cv2.NORM_MINMAX, dtype = cv2.CV_8U)
    img2=resize(img2)
    cv2.imshow('image',img2)
    
    
def power(input_image):
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, 0.4) * 255.0, 0, 255)
    res = cv2.LUT(input_image, lookUpTable)
    res=resize(res)
    cv2.imshow('image',res)
def plotHisto(img):
    plt.hist(img.ravel(),256,[0,256]); plt.show()
    pass
def resize(input_image):
        scale_percent = 60
        width = int(input_image.shape[1] * scale_percent / 100)
        height = int(input_image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(input_image, dim, interpolation = cv2.INTER_AREA)
        return resized
def Hist(input_image):
        
        plotHisto(input_image)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl1 = clahe.apply(img)
        res = np.hstack((input_image, cl1)) 
        res=resize(res)
        plotHisto(res)
        cv2.imshow('image1', res)

img = cv2.imread('histo.tif',0)
