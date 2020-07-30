"""Displays the video""" 

### This code is without the code refactoring 


import cv2

import pygame
import sdl2
import sdl2.ext
sdl2.ext.init()
import time

W = 640
H = 360


window = sdl2.ext.Window("Slam !", size = (W, H), position = (-300, 300))
window.show()

def process_frame(img):

  img = cv2.resize(img , (W, H))
  events = sdl2.ext.get_events()

  for event in events:
  	if event.type == sdl2.SDL_QUIT:
  		exit(0)

  print(dir(window))

  #draw
  surf = sdl2.ext.pixels3d(window.get_surface())
  surf[:, :, 0:3] = img.swapaxes(0, 1)
  #blit
  window.refresh()

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

