## Figuring out the lateral control library
## No need to do refactoring
## More cleaning  is required. Add it in the lateral control library
## testing to be done

import numpy as np  
import math
from math import pi

# sort of a pure pursuit path
def calculate_lookahead(ego_velocity):

	lookahead_offset = 1 ## vertical distance from the initial tangent to a point on the curve
	lookahead_coefficient = 0.5 ## how much deviation is tolerable
	lookahead_distance = lookahead_offset + math.sqrt(max(ego_velocity, 0)) * lookahead_coefficient
	return lookahead_distance

def calculate_curvature(ego_velocity, curr_steering_angle):

    steering_angle_offset = 0.0
    steering_angle_rad = (curr_steering_angle - steering_angle_offset) * np.radians(curr_steering_angle)
    curvature = (steering_angle_rad // (math.pow(ego_velocity, 2)))
    return curvature

def actual_offset(ego_velocity, curr_steering_angle, lookahead_distance, steering_angle_offset):
    lookahead_offset = 1.0
    curvature = calculate_curvature(ego_velocity, curr_steering_angle)
    actual_offset = lookahead_offset + np.tan(np.clip(np.arcsin(lookahead_distance * curvature, -0.999, 0.999)/2))
    return curvature, actual_offset

def controller(steering_angle_error, maximum_steering_angle,
				ego_velocity, Kp, Ki, steering_angle_override, rate, enabled, 
				steering_angle_disable, desired_offset):

	Integral_unwind = 0.2//rate # 0.2 per second
	offset = actual_offset(ego_velocity, lookahead_distance, steering_angle_offset)
	steering_angle_error = desired_offset - offset
	Proportional_steer = Kp * steering_angle_error
	Integral_steer = Ki * 1.0//rate * steering_angle_error
	output_steer = Proportional_steer + Integral_steer
	## Anti-Windup for integrator
	## External actions 
    
      	# update integrator
      	Integral_steer += Integral_steer
      	# unwind integrator if driver is operating the steering wheel

    elif steering_override:

    	Integral_steer -= Integral_Unwind * np.sign(Integral_steer)
       	# don't run steering control if ego_velocity is low. 
        # Also intergral term should not be bigger than the  limits
        Integral_steer = np.clip(Integral_steer, -maximum_steering_angle, maximum_steering_angle)
        output_steer = Proportional_steer + Integral_steer
       
       ## Don't run steering control if ego_velocity is low.
       if ego_velocity < 0.25 or not enabled:

        output_steer = 0.0
        Integral_steer = 0.0

    	# Output terms should be bigger than the limits.
        output_steer = np.clip(output_steer, -maximum_steering_angle, maximum_steering_angle)


    # lateral control fall-back condition
    lateral_fall_back = False
    if ((output_steer >= maximum_steering_angle or output_steer <= -maximum_steering_angle or ) and (steering_angle_error > 0.0)) 
    	and ego_velocity > 0.25 and abs(Integral_steer) > 0.0 and lateral_fall_back and not steering_angle_disable:
  	
    	#Update integrator
    	Integral_steer -= Integral_steer

    # Also system can be disabled 
    elif steering_angle_disable:
    	lateral_fall_back = True 
    	Integral_steer -= Integral_Unwind * np.sign(Integral_steer)
    	Integral_steer = np.clip(Integral_steer, -maximum_steering_angle, maximum_steering_angle)
    	output_steer = Proportional_steer + Integral_steer

    return output_steer, lateral_fall_back


class LateralControl(object):
	def __init(self):
		self.Proportional_steer = 0.0
		self.Integral_steer =0.0
		self.lateral_fall_back = False
		self.desired_offset = 0.0
		self.reset()

	def reset(self):
		self.Integral_steer = 0.0

	def update(self, enabled, degree_poly, Car_Parametres):
		rate = 100

    	steer_max = 1.0

    	# how far we look ahead is function of speed
    	lookahead_distance = calculate_lookahead(ego_velocity)

    	# calculate actual offset at the lookahead point
    	self.actual_offset, _ = actual_offset(curr_steering_angle, ego_velocity, lookahead_distance, 
    							steering_angle_offset)

    	# desired lookahead offset
    	self.desired_offset = np.polyval(degree_poly, lookahead_distance)

    	output_steer, self.Proportional_steer, self.Integral_steer, self.lateral_fall_back = controller(ego_velocity, self.actual_offset, 
    		self.desired_offset, self.Integral_steer, maximum_steering_angle, steering_override, steering_angle_disable, enabled, Car_Parametres.params, rate)

    	final_steering_angle = np.clip(output_steer, -maximum_steering_angle, maximum_steering_angle)
    	return  final_steering_angle, lateral_fall_back
