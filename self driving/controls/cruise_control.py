## Code needs to be fixed. Not final.
""" Design a cruise control system where the driver's state is taken in as input and then the system performs automated CC.
Features to be included are: - 1) if the driver is above a certain speed, then turn on CC, otherwise abort. 2) Abortion will remain manual.
2) the cruise controller needs to perform the following:- 1) regulate during disturbances in road. 2) The controller
 compensates for these unknowns by measuring the speed
# of the car and adjusting the throttle appropriately.
# Device a fall back condition where the driver is ready to take back control at any time manually"""


import math
from math import pi
import numpy as np  
from math import copysign, sin

def vehicle_update(Car_parametres = {}, SYSTEM_INPUT, x, time):
	
    # setting up the system Parametres
    m = Car_parametres.get('m', 1600.)
    g = Car_parametres.get('g', 9.8)
    Cr = Car_parametres.get('Cr', 0.01)
    Cd = Car_parametres.get('Cd', 0.32)
    rho = Car_parametres.get('rho', 1.3)
    A = Car_parametres.get('A', 2.4)
    alpha = Car_parametres.get(
        'alpha', [40, 25, 16, 12, 10])      # gear ratio / wheel radius

	sign = lambda x: copysign(1,x)
	ego_velocity = x[0]
	gear = SYSTEM_INPUT[1]
	theta = SYSTEM_INPUT[2]


    omega = alpha[int(gear)-1] * ego_velocity      # engine angular speed
    F = alpha[int(gear)-1] * motor_torque(omega, Car_parametres) * throttle
    Fg = m * g * sin(theta)   
    Fr  = m * g * Cr * sign(ego_velocity)
    Fa = 1/2 * rho * Cd * A * abs(ego_velocity) * ego_velocity
    # Final acceleration on the car
    Fd = Fg + Fr + Fa
    d = (F - Fd) / m
    
    return d

def motor_torque(omega, Car_parametres = {}):
	# Set up the system parameters
    Tm = Car_parametres.get('Tm', 190.)             # engine torque constant
    omega_m = Car_parametres.get('omega_m', 420.)   # peak engine angular speed
    beta = Car_parametres.get('beta', 0.4)          # peak engine rolloff

    return np.clip(Tm * (1 - beta * (omega/omega_m - 1)**2), 0, None)


# def Transfer_Function():
# 	# design a transfer function  with a PI roll off
# 	Kp = 0.4
# 	Ki = 0.1
# 	tf = kp + 0.01 * Ki
# 	return tf
# 	# In update construct the closed loop system


# We add to this model a feedback controller that attempts to regulate the
# speed of the car in the presence of disturbances. We shall use a
# proportional-integral controller


def pi_controller(ego_velocity, SYSTEM_INPUT, time, x):

	
	#get the controller parametres
	kp = Car_parametres.get('kp', 0.1)
	ki = Car_parametres.get('kg', 2) # Anti windup gain

	#Assign variables for inputs and states
	ego_velocity = SYSTEM_INPUT[0]
	reference_velocity = SYSTEM_INPUT[1]
	z = x[0] # integrated error
	
	return (kp * (reference_velocity - ego_velocity) + (ki *z))
	
# Design a state space controller
def cruise(ego_velocity, antiwindup = False, sys ):

	# Figure out the  bounds and indices
	# add the braek point
    ego_velocity_min = reference_velocity - 1.2; 
    ego_velocity_max = reference_velocity + 0.5; 
    ego_velocity_ind = sys.find_output('ego_velocity')
    SYSTEM_INPUT_min = 0; 
    SYSTEM_INPUT_max = 2 

    if antiwindup:
    	else 1; 

    u_ind = sys.find_output('u')

    # Make sure the upper and lower bounds on v are OK
    while max(y[ego_velocity_ind]) > ego_velocity_max: ego_velocity_max += 1
    while min(y[ego_velocity_ind]) < ego_velocity_min: ego_velocity_min += 1

    return cruise

class CruiseControl(object):
	def __init():
		self.kp = 0.0
		self.ki = 0.0
		self.reference_velocity = 0.0

def update():

	rate = 100
	# calculate the torque as a function of omega, ego_velocity
	torque = motor_torque(ego_velocity, omega_m )
	self.new_cruise = cruise(ego_velocity, rate , reference_velocity, kp, ki, z, sys, SYSTEM_INPUT, x , time)
	final_cruise = np.clip(new_cruise, -SYSTEM_INPUT_max, SYSTEM_INPUT_max)
	return final_cruise
