""" Developing an adaptive cruise control. Firstly, we compute the distance, them calculate the gas and brake pedal positions according to the 
max distance. Accelerate or decelerate to a position using a pi control. Check for integral windup and accelerate to that position by updating
update - with anti windup protection.
"""

import numpy as np  
import math
from numpy import pi 

def calculate_distance (ego_velocity):

	offset_distance = 1.
	lateral_coefficient = 4.
	distance = offset_distance + math.sqrt(max(ego_velocity, 0)) * lateral_coefficient
	return distance

def control_break_pedal(ego_velocity, lateral_acceleration, max_acceleration, Car_parametres, rate):
	
	max_distance = calculate_distance(ego_velocity, time, Car_parametres)	
	break_pedal_position = 0.0
	if (distance <= max_distance):

		break_pedal_position += break_pedal_position_max
		break_pedal_position = break_pedal_position_max

	if (break_pedal_position > 0.0 and (break_pedal_position <= break_pedal_position_max)):		
		## update deceleration if brakes are activated and calc new ego velocity
		deceleration =- lateral_acceleration	

		break_pedal_position = break_pedal_position_max

	if(break_pedal_position < = 0 ) or not enabled:

		## Do not allow car to accelerate. 

		lateral_acceleration -= break_pedal_position_max * np.sign(lateral_acceleration)

	# Still the acceleration should not be bigger than the limits
	lateral_acceleration = np.clip(lateral_acceleration, -max_acceleration, max_acceleration)

	return deceleration


def control_gas_pedal(ego_velocity, lateral_acceleration, enabled,  max_acceleration, Car_parametres):

	gas_pedal_position = 0.0

	max_distance = calculate_distance(ego_velocity, time, Car_parametres)

	if (distance > max_distance ):

		gas_pedal_position +=gas_pedal_position_max
		gas_pedal_position = gas_pedal_position_max

	if (gas_pedal_position <= gas_pedal_position_max and (gas_pedal_position > 0.0)) and not gas_override:

		## update new acceleration
		new_acceleration += lateral_acceleration

	gas_pedal_position = gas_pedal_position_max

	elif gas_override:

		lateral_acceleration -= gas_pedal_position_max * np.sign(lateral_acceleration)


	## Still the acceleration should not be bigger than the limits
	lateral_acceleration = np.clip(lateral_acceleration, -max_acceleration, max_acceleration)

	return new_acceleration


def pi_controller (max_acceleration, acceleration_error, Kp, Ki, enabled ,acceleration_override, rate):



	Integral_unwind = 0.2/rate

	acceleration_error = new_acceleration - deceleration
  	Proportional_acceleration = acceleration_error * Kp
  	Integral_acceleration = acceleration_error * Ki * 1.0/rate
  	Output_acceleration =  Proportional_acceleration + Integral_acceleration

  	""" Anti wind up for integrator part"""

	if((acceleration_error >= 0.0 and (Output_acceleration < max_acceleration or Integral_acceleration < 0.0)) or 
	   (acceleration_error <= 0.0 and (output_accelerationing > -max_acceleration or Integral_acceleration > 0.0))) and not acceleration_override:

	#update integrator
    Integral_accln = Integral_acceleration

  	# unwind integrator if driver is maneuvering the gas pedal
  	elif acceleration_override:

    	Integral_acceleration -= Integral_Unwind * np.sign(Integral_acceleration)
  		# don't run cruise control if ego_velocity is low. 

  	# still, intergral term should not be bigger than the  limits
  	Integral_accln = np.clip(Integral_accln, -max_acceleration, max_acceleration)

  	output_acceleration = Proportional_steer + Integral_accln

  	## Don't activate cruise control if ego_velocity is low.

  	if ego_velocity < 25 or not enabled:

  		output_acceleration = lateral_acceleration
  		Integral_accln = 0.0

  	# Output terms should be bigger than the limits.
  	output_acceleration = np.clip(output_acceleration, -max_acceleration, max_acceleration)

def reset(self):

	self. Integral_accln = 0


def update(self, enabled, ego_velocity, lateral_acceleration, acceleration_override):

	rate = 100

    max_acceleration = 3.5

    # calculate the distance as a function of speed
    distance = calculate_distance(ego_velocity)

    # calculate original acceleration
    self.new_acceleration, _ = control_gas_pedal(ego_velocity, lateral_acceleration, Car_parametres, distance)
                                                

    
    # how much should we decelerate.
    self. deceleration, _ = control_break_pedal(ego_velocity, lateral_acceleration, Car_parametres, distance)

    output_acceleration, self.Proportional_acceleration, self.Integral_acceleration = pi_controller( ego_velocity, self.deceleration, 
    															self.new_acceleration, self.Integral_steer, max_acceleration, enabled, acceleration_override,
    															Car_Parametres.acclnKp, Car_Parametres.acclnKi, rate)

    final_acceleration = np.clip(output_acceleration, -max_acceleration, max_acceleration)
    return  final_acceleration




