
""" combination  of both slam.py and display.py"""
""" In hre we have used a feature based slam for tracking imaages from one image to the next image """
""" The aim here is to write a better orb extractor. First dertect and then compute """


import cv2
import numpy as np
import pygame
import time 
import numpy as np  


from display import Display  

W = 640
H = 360

disp = Display(W, H)
orb = cv2.ORB_create()
print(dir(orb))

class FeatureExtraction(object):
  #  from geohot
  X = 8 // 2
  Y = 6 // 2

  def __init__(self):
    self.orb = cv2.ORB_create(100)

  def extract(self, img):

    feats = cv2.goodFeaturesToTrack(np.mean(img, axis =2).astype(np.uint8), 3000, qualityLevel = 0.01, minDistance = 3)
    print(feats)
    return feats

  """ # run detect in grid: from  geohot
    y = img.shape[0]//self.X
    x = img.shape[1]//self.Y
    akp = []

    for ry in range(0, img.shape[0], y):
      for rx in range(0, img.shape[1], x):

        img_c = img[ry:ry+y , rx:rx+y]
        kp = self.orb.detect(img_c, None)

        for p in kp:
          p.pt = (p.pt[0] + rx, p.pt[1] + ry)

          akp.append(p)

    return akp """


fe = FeatureExtraction()



def process_frame(img):

  img = cv2.resize(img , (W, H))
  kp = fe.extract(img)
  """ kp, des = orb.detectAndCompute(img, None) """

  for p in kp:

    # u, v = map(lambda x: int(round(x)), p.pt) 
    u, v = map(lambda x: int(round(x)), p[0]) 
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