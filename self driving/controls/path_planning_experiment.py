"""Steps to the algorithm
- get the trajectory
- compute the planned path
- calculate desired path.
- class Pathplanning
- Update """

import numpy as np  

import math


def compute_path():

	deg = 2
	x = np.arange(50.0)
	X = np.vstack(tuple(x**n for n in range(deg, -1, -1)))

	pinv = np.linalg.pinv(X)

def model_polyfit(points, path):

	return np.dot(path, map(float, points))

# Indian Road congress (INC)
V_lane_width = [2.0, 23.5]

# https://nptel.ac.in/content/storage2/courses/105101008/downloads/cete_24.pdf
# Break point of speed
BP_lane_width = [0.0, 7.3]

def calculate_desired_path(l_poly, r_poly, predicted_poly, l_probability, r_probability, predicted_probability, speed):

	# we are dealing with discrete dat points, hence interp function. One dimensional piecewise linear interpolant

	# centre the weighted average

	lane_width = interp(V_lane_width, BP_lane_width, speed)


	## 4 Lane width in india is 23.5m

	half_lane = np.array([0. , 0., 0., lane_width // 2.])


	# 0.5/100 because half lane. Calculate centre poly, centre probability
	if l_probability + r_probability > 0.01:

		centre_poly = (((l_poly - half_lane) * l_probability) + ((r_poly - half_lane ) * r_probability))/ (l_probability + r_probability)
		centre_probability = math.sqrt (l_probability**2 - r_probability**2, 2.0)
	else:

		centre_poly = np.zeros(2.0)
		centre_probability = 0. 

    path_weight = 1.

    desired_poly = list((centre_poly * centre_probability + path_weight * predicted_probability * predicted_poly) / 
    					(centre_probability + path_weight * predicted_poly))

    return desired_poly, centre_probability, centre_poly



class Pathplanning (object):

	def _init(self, model):


		self.model = model
		
		self.d_poly = [0., 0., 0., 0.]
		self.lead_dist, self.lead_probability, self.lead_var = 0, 0, 1
    	self._path_comp = compute_path()

def update(self, ego_velocity):

	  
      predicted_poly = model_polyfit(model.predictedPath.points, self._path_comp)       # predicted path
      l_poly = model_polyfit(model.LeftLane.points,self._path_comp)   # left line
      r_poly = model_polyfit(model.RightLane.points, self._path_comp)  # right line

      predicted_probability = 1.                       # model does not tell this probability yet, so set to 1 for now
      l_prob = model.leftLane.prob   # left line prob
      r_prob = model.rightLane.prob  # right line prob

      self.lead_dist = model.lead.dist
      self.lead_probability = model.lead.prob
      self.lead_var = model.lead.std**2

      # compute target path
      self.desired_poly, _, _ = calculate_desired_path(l_poly, r_poly, predicted_poly, l_prob, r_prob, predicted_probability, ego_velocity)


