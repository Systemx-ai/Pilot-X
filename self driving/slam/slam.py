
""" combination  of both slam.py and display.py"""
""" In hre we have used a feature based slam for tracking imaages from one image to the next image """
""" The aim here is to write a better orb extractor. First dertect and then compute """
"""  Get the features and the matches """

import cv2
import numpy as np
import pygame
import time 
import numpy as np  
from display import Display
from feature_extractor import FeatureExtraction  

W = 640
H = 360

disp = Display(W, H)
orb = cv2.ORB_create()
print(dir(orb))


fe = FeatureExtraction()


def process_frame(img):

  img = cv2.resize(img , (W, H))
  matches = fe.extract(img)
  """ kp, des = orb.detectAndCompute(img, None) """
  
  print("%d matches" % (len(matches)))

  for pt1, pt2 in matches:
    u1,v1 = map(lambda x: int(round(x)), pt1)
    u2,v2 = map(lambda x: int(round(x)), pt2)
    cv2.circle(img, (u1, v1), color=(0,255,0), radius=3)
    cv2.line(img, (u1, v1), (u2, v2), color=(255,0,0))
    

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