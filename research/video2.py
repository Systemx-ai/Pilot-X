import cv2
# print(cv2.__version__)
vidcap = cv2.VideoCapture('sample.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frames//%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  count += 1



