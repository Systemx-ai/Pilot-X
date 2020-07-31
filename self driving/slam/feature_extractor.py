""" Refactored code for feature_extraction"""

import numpy as np 
import time
import cv2


from skimage.measure import ransac
from skimage.transform import FundamentalMatrixTransform


class FeatureExtraction(object):
  #  from geohot
  # X = 8 // 2
  # Y = 6 // 2

  def __init__(self):
    self.orb = cv2.ORB_create(100)

    self.bf =cv2.BFMatcher()
    self.last = None

  def extract(self, img):

    # detection
    feats = cv2.goodFeaturesToTrack(np.mean(img, axis =2).astype(np.uint8), 3000, qualityLevel = 0.01, minDistance = 3)
    
    #extraction
    kps = [cv2.KeyPoint(x = f[0][0], y =f[0][1], _size = 20) for  f in feats]

    
    kps, des = self.orb.compute(img, kps)
    ## we are getting key points and descriptors
    # print(feats)
    # print(kps)

    # matching is done here

    
    matches = None
    ret = []
    if self.last is not None:
      matches = self.bf.knnMatch(des, self.last['des'], k=2)
      for m,n in matches:
        if m.distance < 0.75*n.distance:
          kp1 = kps[m.queryIdx].pt
          kp2 = self.last['kps'][m.trainIdx].pt
          ret.append((kp1, kp2))

    # filter
    if len(ret) > 0:
      ret = np.array(ret)
      model, inliers = ransac((ret[:, 0], ret[:, 1]),
                              FundamentalMatrixTransform,
                              min_samples=8,
                              residual_threshold=1,
                              max_trials=100)
      ret = ret[inliers]

      ## resolving the noise.

    # return
    self.last = {'kps': kps, 'des': des}
    return ret

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
