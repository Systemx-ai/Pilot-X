

""" combination  of both slam.py and display.py"""
""" In hre we have used a feature based slam for tracking imaages from one image to the next image """



import cv2
import numpy as np
import pygame
import time 


from display import Display  


W = 640
H = 360


disp = Display(W, H)
orb = cv2.ORB_create()
print(dir(orb))


def process_frame(img):

  img = cv2.resize(img , (W, H))
  kp, des = orb.detectAndCompute(img, None)

  for p in kp:

    u, v = map(lambda x: int(round(x)), p.pt) 

    cv2.circle(img, (u, v), color = (0, 255, 0), radius = 3)

  disp.paint(img)
  print(img.shape)

if __name__ == '__main__':

	cap = cv2.VideoCapture('test.mp4')


if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
 
  ret, frame = cap.read()
  if ret == True:

    process_frame(frame)
  else:
  	break