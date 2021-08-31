import cv2
import numpy as np
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        mycolorimage=np.zeros((512,512,3),dtype=np.uint8)
        mycolorimage[:]=[blue,green,red]
        cv2.imshow('image',mycolorimage)
img=cv2.imread('original.jpg')
cv2.imshow('Im',img)
points=[]
cv2.setMouseCallback('Im',click_event)
cv2.waitKey()
cv2.destroyAllWindows()
