# Not consistent with test passing


import numpy as np  
import math
from math import pi
from lateral_control import calculate_lookahead, calculate_curvature
from lateral_control import actual_offset
def main():
	ego_velocity = 26
	curr_steering_angle = 200.82
	# lookahead_distance = 9.0
	# lookahead_offset = 1.0
	# steering_angle_offset = 0.0
	sp = calculate_lookahead(ego_velocity)
	ps = calculate_curvature(ego_velocity, curr_steering_angle)


	print(ps)
	print(sp)

if __name__ == '__main__':
	main()

# degree = 45
# c = np.radians(degree)
# print(c)