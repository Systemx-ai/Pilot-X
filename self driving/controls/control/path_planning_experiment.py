"""Steps to the algorithm
- get the trajectory
- compute the planned path
- calculate the best guessed path, by taking the weighted average of the left and right path.
- class Pathplanning
- Update. Based off the work by comma ai """

import numpy as np  
import math

def compute_path():

	deg = 4
	x = np.arange(50.0)
	X = np.vstack(tuple(x**n for n in range(deg, -1, -1))) # vstack() function is used to stack arrays in sequence vertically (row wise).
	pinv = np.linalg.pinv(X)
	return pinv

def model_polyfit(points, path):

	return np.dot(path, map(float, points))

# Indian Road congress (INC)
V_lane_width = [2.0, 23.5]
# https://nptel.ac.in/content/storage2/courses/105101008/downloads/cete_24.pdf
# Break point of speed
BP_lane_width = [0.0, 7.3]

def calculate_desired_path(l_poly, r_poly, predicted_poly, l_probability, r_probability, predicted_probability, speed):

	# we are dealing with discrete data points, hence interp function. One dimensional piecewise linear interpolant. We have to calculate the
	# weighted average of the lane widths, both left and right.
	# centre the weighted average
	lane_width = interp(V_lane_width, BP_lane_width, speed)
	## 4 Lane width in india is 23.5m
	half_lane = np.array([0. , 0., 0., lane_width // 2.])
	# 0.5/100 because half lane. Calculate centre poly, centre probability
	if l_probability + r_probability > 0.01:

		# poly is for centering and scaling values
		centre_polyfit = (((l_poly - half_lane) * l_probability) + ((r_poly - half_lane ) * r_probability))/ (l_probability + r_probability)
		centre_probability = math.sqrt (l_probability**2 - r_probability**2, 2.0)

	else:

		centre_polyfit = np.zeros(4.0)
		centre_probability = 0.
    	
    path_weight = 1.0
    desired_poly = list((centre_polyfit * centre_probability * path_weight + predicted_probability * predicted_poly)/(centre_probability + path_weight * predicted_poly))

    return desired_poly, centre_probability, centre_polyfit

class Pathplanning(object):

	def _init(self, model):		
        self.model = model ## assuming for now
		self.d_poly = [0., 0., 0., 0.]
    	self._path_comp = compute_path()

     def update(self, ego_velocity):

        predicted_polyfit = model_polyfit(model.points, self._path_predicted)# predicted path
        left_polyfit = model_polyfit(model.points,self._path_predicted)# left line
        right_polyfit = model_polyfit(model.points, self._path_predicted)# right line

        predicted_probability = 1.  # model does not tell this probability yet, so set to 1 for now
        l_probability = model.predicted_probability   # left line prob
        r_probability = model.predicted_probability # right line prob

        # compute target path
        self.desired_polyfit, _, _ = calculate_desired_path(left_polyfit, right_polyfit, predicted_polyfit, l_probability, r_probability, 
        													predicted_probability, ego_velocity)