# Not consistent with test passing

import numpy as np  
import path_plan
from path_plan import compute_probability 
from path_plan import model_polyfit
from numpy import interp
import sys

def main():
	
	# Indian Road congress (INC)
	V_lane_width = [2.0, 23.5]
	# https://nptel.ac.in/content/storage2/courses/105101008/downloads/cete_24.pdf
	# Break point of speed
	BP_lane_width = [0.0, 7.3]
	speed = [0.0, 10.0]
	lane_width = interp(V_lane_width, BP_lane_width, speed)
	half_lane = np.array([0. , 0., 0., lane_width // 2.])
	print(lane_width, half_lane)
	left_path_weight = 1.
	right_path_weight = 1.
	l_probability = 0.006
	r_probability = 0.123
	left_polyfit = 0.1
	right_polyfit = 0.22
	ss = compute_probability(speed, left_polyfit, right_polyfit, l_probability, r_probability)
	print(ss)

if __name__ == '__main__':
	 main()