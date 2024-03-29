import numpy as np 
import math
from math import pi 
from numpy import interp

def model_polyfit(path, points):	
	degree = 4 # 4 degree curve
	poly = np.polyfit(path, list(points), 4)
	return poly	
# Indian Road congress (INC)
V_lane_width = [2.0, 23.5]
# https://nptel.ac.in/content/storage2/courses/105101008/downloads/cete_24.pdf
# Break point of speed
BP_lane_width = [0.0, 7.3]

def compute_probability(speed, left_polyfit, right_polyfit, l_probability, r_probability):		
	lane_width = interp(V_lane_width, BP_lane_width, speed)
	# to debug
	if debug:

		print(lane_width)
	half_lane = np.array([0. , 0., 0., lane_width // 2.])
	left_path_weight = 1.
	right_path_weight = 1.
	if l_probability + r_probability > 0.01:
		# polyfit is for centreing and scaling
		centre_polyfit = (((left_polyfit - half_lane ) * l_probability) 
						+ (right_polyfit - half_lane) * r_probability)/ (l_probability + r_probability)
		centre_probability = np.sqrt (l_probability**2 + r_probability**2/2.0)
	else:
		centre_probability = 0.0
		centre_polyfit = np.zeros(4)
	desired_polyfit = (centre_polyfit * centre_probability * right_path_weight  + 
 						centre_polyfit * centre_probability * left_path_weight)/((centre_probability + left_polyfit * left_path_weight + right_polyfit * right_path_weight))
	return centre_probability, desired_polyfit, centre_polyfit

def compute_predicted_path():
	X_path_probability = model_polyfit(poly)
	predicted_path = list((X_path_probability * left_path_weight + X_path_probability * right_path_weight) / 
    					(right_path_weight + left_path_weight))
	return predicted_path
class Pathplanning(object):
	def _init(self, model):		
		self.d_poly = [0., 0., 0., 0.]
		self._path_predicted = compute_predicted_path()
	def update(self, ego_velocity):
		# centre_polyfit = model_polyfit(points, self._path_predicted)
		# left_polyfit = model_polyfit(points,self._path_predicted)
		# right_polyfit = model_polyfit(points, self._path_predicted)
		predicted_probability = 1.
		l_probability = compute_probability(left_path_weight, predicted_probability)
		r_probability = compute_probability(right_path_weight, predicted_probability)
		self.desired_polyfit, _, _ = compute_predicted_path(left_polyfit, right_polyfit, predicted_polyfit, l_probability, r_probability, 
        													predicted_probability, ego_velocity)
		return self.desired_polyfit
		
"""# take the discrete points in as input
# path = np.arange(20)
# points = np.arange(20)
# degree = 4.0 # 4 degree curve
# poly = np.polyfit(path, list(points), degree)
# print(poly)"""


"""# import numpy as np 
# import math
# from math import pi 
# from numpy import interp

# # take the discrete points in as input
# path = np.arange(0.0, 20.0)
# degree = 4 # 4 degree curve

# def model_polyfit():

# 	poly = np.polyfit(path, degree)
# 	return poly

# # Indian Road congress (INC)
# V_lane_width = [2.0, 23.5]
# # https://nptel.ac.in/content/storage2/courses/105101008/downloads/cete_24.pdf
# # Break point of speed
# BP_lane_width = [0.0, 7.3]
# speed = [0.0, 10.0]
# lane_width = interp(V_lane_width, BP_lane_width, speed)
# half_lane = np.array([0. , 0., 0., lane_width // 2.])
# # print(lane_width, half_lane)
# left_path_weight = 1.
# right_path_weight = 1.
# l_probability = 0.006
# r_probability = 0.12223
# left_polyfit = 0.1
# right_polyfit = 0.22
# if l_probability + r_probability > 0.01:
# 	# polyfit is for centreing and scaling
# 	centre_polyfit = (((left_polyfit - half_lane ) * l_probability) 
# 						+ (right_polyfit - half_lane) * r_probability)/ (l_probability + r_probability)
	
# 	#print(centre_polyfit)
# 	centre_probability = np.sqrt((l_probability**2 + r_probability**2)/2.)
# 	print(centre_probability)
# else:
# 	centre_probability = 0.0
# 	centre_polyfit = np.zeros(4)

# 	desired_polyfit = (centre_polyfit * centre_probability * right_path_weight  + 
# 						centre_polyfit * centre_probability * left_path_weight)/((centre_probability + left_polyfit * left_path_weight + right_polyfit * right_path_weight))

# 	print(desired_polyfit)"""
