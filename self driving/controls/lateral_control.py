# Algorithm, yet to go through proper testing
""" Algo will go through proper  testing in later versions. 
	Do not try to test for now. Will be updated with each tag. Geometric lateral Control. Work is loosely based on comma ai 's 
	lateral control. first calculate the curvature and then  calculate the lookahead distance and then compute the lookahead offset. 
	Then steer the vehicle to that position by closing the loop using a pi controller. check for integral windup, then steer it to that 
	position by updating (with anti windup protection).  
	"""

import math


import numpy as np   
import matplotlib.pyplot  as   plt 

from math import pi
 

def calculate_curvature(ego_velocity, steer_angle, Car_Parametres, offset_angle = 0):

	degree_to_rad = np.pi/180.0

	steer_angle_rad = (steer_angle - offset_angle) * degree_to_rad
	curvature = steer_angle_rad/((Car_Parametres.Wheelbase * Car_Parametres.Steering_ratio * 
								(1 + Car_Parametres.slip_factor * math.pow(max(ego_velocity,2)) )))

	return curvature

def pi_controller(steer_error, max_steer, steer_override, Integral_steer, enabled, 
				 Kp, Ki, rate, actual_Offset, desired_offset):


  	Integral_Unwind = 0.2/rate 

  	""" 0.2 per second"""
	
  	steer_error = desired_offset - actual_Offset
  	Proportional_steer = steer_error * Kp
  	Integral_steering = steer_error * Ki * 1.0/rate
  	Output_steering = Proportional_steer + Integral_steering

  	""" Anti wind up for integrator part"""

	if((steer_error >= 0.0 and (Output_steering < max_steer or Integral_steer < 0.0)) or 
	   (steer_error <= 0.0 and (Output_steering > -max_steer or Integral_steer > 0.0))) and not steer_override:

	#update integrator
    Integral_steer = Integral_steering

  	# unwind integrator if driver is maneuvering the steering wheel
  	elif steer_override:

    	Integral_steer -= Integral_Unwind * np.sign(Integral_steer)
  		# don't run steer control if ego_velocity is low. 

  	# still, intergral term should not be bigger than the  limits
  	Integral_steer = np.clip(Integral_steer, -max_steer, max_steer)

  	output_steer = Proportional_steer + Integral_steer

  	## Don't run steering control if ego_velocity is low.

  	if ego_velocity < 0.2 or not enabled:

  		output_steer = 0.0
  		Integral_steer = 0.0

  	# Output terms should be bigger than the limits.
  	output_steer = np.clip(output_steer, -max_steer, max_steer)




def calculate_lookahead(ego_velocity):


	lookahead_offset = 1.
	lookahead_coefficient = 4.4

	
""" Calculating the lookahead distance l_d. Geometric 
	lateral control. (Using the bicycle model) """

	lookahead_distance = lookahead_offset + math.sqrt(max(ego_velocity, 0)) * lookahead_coefficient

	return lookahead_distance

def calculate_lookahead_offset(ego_velocity, steer_angle, lookahead_distance, Car_Parametres, offset_angle):

	#this function returns the lateral offset given the steering angle, speed and the lookahead distance
  

	curvature = calculate_curvature(ego_velocity, steer_angle, Car_Parametres, offset_angle)
  

  	# clip is to avoid arcsin NaNs due to too sharp turns
 	actual_Offset = lookahead_distance * np.tan(np.clip(np.arcsin(lookahead_distance * curvature, -0.999, 0.999)/2))                         
  	return actual_Offset, curvature


def reset(self):

	self. Integral_steer = 0


def update(self, enabled, ego_velocity, steer_angle, steer_override):

	rate = 100

    max_steer = 1.0

    # how far we look ahead is function of speed
    lookahead_distance = calculate_lookahead(ego_velocity)

    # calculate actual offset at the lookahead point
    self.actual_Offset, _ = calculate_lookahead_offset(ego_velocity, steer_angle,
                                                lookahead_distance, Car_Parametres, offset_angle)

    # desired lookahead offset
    self.desired_offset = np.polyval(d_poly, lookahead_distance)

    output_steer, self.Proportional_steer, self.Integral_steer = pi_controller( ego_velocity, self.actual_Offset, self.desired_offset, 
    															self.Integral_steer, max_steer, steer_override, enabled, 
    															Car_Parametres.steerKp, Car_Parametres.steerKi, rate)

    final_steer = np.clip(output_steer, -max_steer, max_steer)
    return final_steer





                                                                                   



