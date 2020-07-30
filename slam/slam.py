
import cv2
import numpy as np
import pygame

import tensorflow as tf   




W = 720//4
H = 1280//4

pygame.init()
screen = pygame.display.set_mode((W, H))
surface = pygame.Surface((W,H)).convert()

def process_frame(img):
	img = cv2.resize(img , (W, H))
	

	surf = pygame.surfarray.make_surface(img).convert()
	screen.blit(surf, (0, 0))
	pygame.display.flip()

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






