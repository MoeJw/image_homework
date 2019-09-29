from PIL import Image, ImageDraw
import cv2
import numpy as np
def value(input_image,input_pixels,offset,l,draw):
    for x in range(offset, input_image.width - offset):
        for y in range(offset, input_image.height - offset):
            acc=0
            for a in range(len(l)):
                for b in range(len(l)):
                    xn = x + a - offset
                    yn = y + b - offset
                    pixel = input_pixels[xn, yn]
                    acc+= pixel * l[a][b]
            draw.point((x, y), (int(acc), int(acc), int(acc)))

def filter(type):
    input_image = Image.open("histo.tif")
    input_pixels = input_image.load()
    img2 = cv2.imread('histo.tif',0)
    l=[]
    if(type==1):
            for y in range(3):
             l.append(map(float,raw_input("enter  row"+str(y+1)+" coefficients :").split()))  
    if(type==2):
        l=[[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]]
    elif(type==3):
        #l = [[1/16.0, 2/16.0, 1/16.0],[2/16.0, 4/16.0, 2/16.0],[2/16.0, 2/16.0, 1/16.0]]
        l=[[1/9.0, 1/9.0, 1/9.0],[1/9.0, 1/9.0, 1/9.0],[1/9.0, 1/9.0, 1/9.0]]
    print(l)

    offset = len(l) // 2


    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)
    value(input_image,input_pixels,offset,l,draw)
    
    
        
    output_image.save("output.tif")                                          


#l = [[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]]
#l = [[1/16.0, 2/16.0, 1/16.0],[2/16.0, 4/16.0, 2/16.0],[2/16.0, 2/16.0, 1/16.0]]
print("1- enter  coefficients of the mask")
print("2-Enhancement Using the Laplacian")
print("3-unsharp Masking")
type=int(raw_input("enter Number : "))

filter(type)
img = cv2.imread('output.tif',0)
img2 = cv2.imread('histo.tif',0)
if(type==3):
    res = np.hstack(((img2-img)+img2, img2))
else:
    res = np.hstack((img, img2))


cv2.imshow("output_image",res)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    
