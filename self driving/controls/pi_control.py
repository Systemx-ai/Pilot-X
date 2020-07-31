""" 1. Refactor the lateral control code.
2. combine the two in original lateral control.py"""


import math
import numpy as np 

class Picontrol(object):

	def __init__(self):
		
		self.Proportional_steer = 0.0
		self.Integral_steer = 0.0
		self.desired_offset = 0.0
		self.Integral_steer = 0.0
		self.reset()
  
  def reset(self):

		self.Integral_steer = 0
	
  def controller(steer_error, max_steer, steer_override, Integral_steer, enabled, 
				 Kp, Ki, rate, actual_Offset, desired_offset):


  		Integral_Unwind = 0.2/rate 

  		""" 0.2 per second"""
	 	  ## integer 
  		steer_error = desired_offset - actual_Offset
  		Proportional_steer = steer_error * Kp
  		Integral_steering = steer_error * Ki * 1.0//rate
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




